#import thư viện :3

import base64
import json
from getpass import getpass 

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


# Salt size tính bằng byte
SALT_SIZE = 16
# Số vòng lặp cho PBKDF2. Càng cao càng an toàn nhưng càng chậm.
ITERATIONS = 100000
# Kích thước khóa AES tính bằng byte (256 bit = 32 byte)
KEY_SIZE = 32
# Kích thước Nonce tính bằng byte
NONCE_SIZE = 12

def encrypt(password: str, plaintext: str) -> str:

    #Encode bằng AES-256-GCM sử dụng mật khẩu.

    try:
        
        salt = get_random_bytes(SALT_SIZE)

        
        key = PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)

        
        plaintext_bytes = plaintext.encode('utf-8')

        
        cipher = AES.new(key, AES.MODE_GCM, nonce=get_random_bytes(NONCE_SIZE))
        
        
        ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)

        
        encrypted_data = {
            'salt': base64.b64encode(salt).decode('utf-8'),
            'nonce': base64.b64encode(cipher.nonce).decode('utf-8'),
            'tag': base64.b64encode(tag).decode('utf-8'),
            'ciphertext': base64.b64encode(ciphertext).decode('utf-8')
        }
        
        
        json_string = json.dumps(encrypted_data)
        
        print("\nEncrypt Thành Công.")
        return json_string

    except Exception as e:
        print(f"\nĐã có bug: {e}")
        return None

def decrypt(password: str, encrypted_json_string: str) -> str:

    #Decode dữ liệu đã mã hóa bằng AES-256-GCM.

    try:

        encrypted_data = json.loads(encrypted_json_string)
        
        salt = base64.b64decode(encrypted_data['salt'])
        nonce = base64.b64decode(encrypted_data['nonce'])
        tag = base64.b64decode(encrypted_data['tag'])
        ciphertext = base64.b64decode(encrypted_data['ciphertext'])
        
        key = PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)

        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        

        decrypted_bytes = cipher.decrypt_and_verify(ciphertext, tag)
        
        plaintext = decrypted_bytes.decode('utf-8')
        
        print("\nDecrypt Thành Công.")
        return plaintext

    except (ValueError, KeyError) as e:
        # bug xảy ra khi dữ liệu lỗi hoặc pass có vấn đề
        print("\nBug Decrypt: Mật khẩu không đúng hoặc dữ liệu đã bị thay đổi!")
        return None
    except Exception as e:
        print(f"\nĐã có Bug: {e}")
        return None


if __name__ == '__main__':
    while True:
        choice = input("\nBạn muốn (1) Mã hóa hay (2) Giải mã? (Nhấn Enter để thoát): ")
        if choice == '1':
            password = input("Nhập mật khẩu để MÃ HÓA (Lưu ý mật khẩu nhập vào sẽ bị che để đảm bảo bảo mật): ")
            plaintext = input("Nhập dữ liệu bạn muốn mã hóa: ")
            if not password or not plaintext:
                print("Mật khẩu và dữ liệu không được để trống!")
                continue
            
            encrypted_output = encrypt(password, plaintext)
            if encrypted_output:
                print("\n--- DỮ LIỆU ĐÃ MÃ HÓA ---")
                print("Lưu lại TOÀN BỘ chuỗi dưới đây để giải mã:")
                print(encrypted_output)
                print("---------------------------\n")

        elif choice == '2':
            password = input("Nhập mật khẩu để GIẢI MÃ (Lưu ý mật khẩu nhập vào sẽ bị che để đảm bảo bảo mật): ")
            encrypted_input = input("Dán toàn bộ dữ liệu đã mã hóa vào đây: ")
            if not password or not encrypted_input:
                print("Mật khẩu và dữ liệu đã mã hóa không được để trống!")
                continue

            decrypted_output = decrypt(password, encrypted_input)
            if decrypted_output:
                print("\n--- DỮ LIỆU GỐC ---")
                print(decrypted_output)
                print("--------------------\n")
        else:
            print("Đã thoát chương trình.")

            break


