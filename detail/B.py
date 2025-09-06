# chat_client.py
import requests
import time
import os

# url của mình
MY_SERVER_URL = "http://127.0.0.1:5000"

# url của ngta
PARTNER_NGROK_URL = "https://thay-dia-chi-ngrok-cua-ban-chat-vao-day.ngrok-free.app"


def send_message(message_text):
    """Gửi tin nhắn lên server của chính mình."""
    try:

        response = requests.post(f"{MY_SERVER_URL}/send", json={"message": message_text})
        if response.status_code == 200:
            print(f"Bạn: {message_text}")
        else:
            print(f"[Lỗi] Không thể gửi tin nhắn. Mã lỗi: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("[Lỗi] Không thể kết nối tới server của chính mình. Bạn đã chạy file chat_server.py chưa?")

def receive_message():
    """Lấy tin nhắn từ server của đối tác."""
    try:

        response = requests.get(f"{PARTNER_NGROK_URL}/get_message")
        if response.status_code == 200:
            data = response.json()
            return data.get("message", "Không nhận được tin nhắn.")
        else:
            return f"[Lỗi] Không thể lấy tin nhắn. Mã lỗi: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"[Lỗi] Không thể kết nối tới server của đối tác. Hãy kiểm tra lại URL ngrok."

def main():
    """Vòng lặp chính của chương trình chat."""
    partner_last_message = ""
    while True:

        my_new_message = input("Nhập tin nhắn của bạn và nhấn Enter (gõ 'exit' để thoát): ")
        if my_new_message.lower() == 'exit':
            break
        send_message(my_new_message)
        

        print("...")
        time.sleep(2) 
        
        current_partner_message = receive_message()

        if current_partner_message != partner_last_message:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("--- CUỘC TRÒ CHUYỆN ---")
            print(f"Đối tác: {current_partner_message}")
            partner_last_message = current_partner_message
        
        print("------------------------")

# :)
if __name__ == "__main__":
    main()
