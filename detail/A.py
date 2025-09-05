import socket

# 1. Khởi tạo socket
# AF_INET dùng cho IPv4, SOCK_STREAM dùng cho TCP (giao thức tin cậy)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Cấu hình địa chỉ và cổng
# '0.0.0.0' có nghĩa là lắng nghe từ tất cả các địa chỉ IP của máy
# Chọn một cổng bất kỳ, ví dụ 65432
HOST = '0.0.0.0'
PORT = 65432

# Sử dụng một khối try-except để xử lý lỗi
try:
    server.bind((HOST, PORT))
    
    # 3. Lắng nghe kết nối đến (tối đa 1 kết nối chờ)
    server.listen(1)
    print(f"Máy B đang lắng nghe ở cổng {PORT}...")

    # 4. Chờ và chấp nhận kết nối từ máy A
    conn, addr = server.accept()
    print(f"Máy B đã kết nối với: {addr[0]} (IP) và {addr[1]} (Port)")

    # 5. Nhận dữ liệu
    print("Bắt đầu nhận file...")
    with open("received_file.dat", "wb") as f:
        while True:
            # Nhận từng phần dữ liệu (chunk)
            # Kích thước buffer 4096 byte
            data = conn.recv(4096)
            if not data:
                break  # Kết thúc khi không còn dữ liệu
            f.write(data)

    print("Đã nhận file thành công!")

except socket.error as e:
    print(f"Lỗi: {e}")

finally:
    # Đóng kết nối
    conn.close()
    server.close()
    print("Đã đóng kết nối.")
