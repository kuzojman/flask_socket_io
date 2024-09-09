import requests
from socketio import Client

sio = Client()

@sio.event
def connect():
    print("Connection established")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.on("response")
def handle_response(data):
    if data["status"] == "Number sent to Flask app":
        print("Number sent successfully!")
    else:
        print("Error:", data["error"])

response = requests.get("http://localhost:5000")
csrf_token = response.cookies.get("csrf_token")

sio.connect("http://localhost:5006", headers={"Cookie": f"csrf_token={csrf_token}"})

sio.emit("send_number", {"number": 19888})

sio.disconnect()