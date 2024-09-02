import socketio

# Создаем клиента SocketIO
sio = socketio.Client()

# Добавляем обработчик событий для подключения
@sio.event
def connect():
    print("Connection established")

# Добавляем обработчик событий для ошибок подключения
@sio.event
def connect_error(data):
    print("The connection failed!")

# Добавляем обработчик событий для отключения
@sio.event
def disconnect():
    print("Disconnected from server")

# Подключаемся к приложению на порту 5006
sio.connect('http://localhost:5006')

# Отправляем число
sio.emit('send_number', {'number': 15634})

# Закрываем соединение
sio.disconnect()