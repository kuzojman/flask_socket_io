from flask import Flask
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "SocketIO server running"

@socketio.on('send_number')
def handle_number(data):
    number = data['number']
    # Отправляем POST-запрос в Flask-приложение
    requests.post('http://localhost:5000/update', data={'number': number})
    emit('response', {'status': 'Number sent to Flask app'})

if __name__ == '__main__':
    socketio.run(app, port=5006, host='0.0.0.0')