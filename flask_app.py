from flask import Flask, render_template, request, jsonify, session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key_here"  # замените на случайный ключ
csrf = CSRFProtect(app)

received_data = None

@app.route("/")
def index():
    global received_data
    return render_template("index.html", number=received_data)

@app.route("/update", methods=["POST"])
@csrf.exempt  # исключение для POST-запроса из SocketIO
def update():
    global received_data
    received_data = request.form["number"]
    print(received_data)
    return "Updated", 200

@app.route("/get_number", methods=["GET"])
def get_number():
    return jsonify({"number": received_data})

if __name__ == "__main__":
    app.run(port=5000)