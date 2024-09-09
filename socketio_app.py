from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key_here"  # тот же ключ, что и в flask_app
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("connect")
def handle_connect():
    print("Connection established")

@socketio.on("disconnect")
def handle_disconnect():
    print("Disconnected from server")

@socketio.on("send_number")
def handle_number(data):
    number = data["number"]
    csrf_token = request.cookies.get("csrf_token")  # получаем токен из cookie
    headers = {"X-CSRFToken": csrf_token}  # добавляем токен в заголовок
    response = requests.post("http://localhost:5000/update", data={"number": number}, headers=headers)
    if response.status_code == 200:
        emit("response", {"status": "Number sent to Flask app"},broadcast=True)
    else:
        emit("response", {"status": "Error sending number", "error": response.text})

if __name__ == "__main__":
    socketio.run(app, port=5006, host="0.0.0.0")