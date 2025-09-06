# chat_server.py
from flask import Flask, request, jsonify


app = Flask(__name__)


my_message = "Chưa có tin nhắn nào."


@app.route('/')
def home():
    """Hiển thị tin nhắn hiện tại dưới dạng HTML."""
    return f"<h1>Tin nhắn hiện tại là:</h1><p>{my_message}</p>"


@app.route('/send', methods=['POST'])
def send():
    """Nhận và cập nhật tin nhắn mới."""
    global my_message

    data = request.get_json()
    if data and 'message' in data:
        my_message = data['message']
        print(f"-> Đã cập nhật tin nhắn của mình thành: '{my_message}'")
        return jsonify({"status": "success", "message": "Tin nhắn đã được cập nhật."})
    return jsonify({"status": "error", "message": "Dữ liệu không hợp lệ."}), 400

# cho cái máy của đối tác lấy tin nhắn ấy
@app.route('/get_message')
def get_message():
    """Cung cấp tin nhắn hiện tại dưới dạng JSON."""
    return jsonify({"message": my_message})


if __name__ == '__main__':
    # run trên all các address IP có sẵn của máy, cổng à 5000
    app.run(host='0.0.0.0', port=5000)
