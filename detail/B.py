
import socket
import os

# 1. Khởi tạo socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Cấu hình địa chỉ và cổng của máy B
# Thay đổi 'YOUR_PUBLIC_IP' bằng IP công cộng của máy B
HOST = 'YOUR_PUBLIC_IP'
PORT = 65432

# Tên file cần gửi
FILE_TO_SEND = "file_to_send.dat"

try:
    # 2. Kết nối tới máy B
    client.connect((HOST, PORT))
    print("Máy A đã kết nối thành công tới máy B.")

    # 3. Mở và gửi file
    print(f"Bắt đầu gửi file '{FILE_TO_SEND}'...")
    with open(FILE_TO_SEND, "rb") as f:
        while True:
            # Đọc từng phần dữ liệu từ file
            data = f.read(4096)
            if not data:
                break
            client.sendall(data) # Gửi tất cả dữ liệu đã đọc

    print("Đã gửi file thành công!")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{FILE_TO_SEND}' để gửi.")
except socket.error as e:
    print(f"Lỗi: {e}")

finally:
    # Đóng kết nối
    client.close()
    print("Đã đóng kết nối.")
