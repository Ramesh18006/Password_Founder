from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

DEMO_PASSWORD = os.environ.get("DEMO_PASSWORD", "417")


@app.route("/")
def home():
    return send_from_directory(".", "password.html")


@app.route("/style.css")
def stylesheet():
    return send_from_directory(".", "style.css")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    entered_password = data.get("password", "")

    if not isinstance(entered_password, str) or len(entered_password) != 3 or not entered_password.isdigit():
        return jsonify({
            "success": False,
            "message": "Enter exactly 3 digits."
        }), 400

    if entered_password == DEMO_PASSWORD:
        return jsonify({
            "success": True,
            "message": "Login Successful!"
        })

    return jsonify({
        "success": False,
        "message": "Incorrect Password. Try Again."
    }), 401


if __name__ == "__main__":
    app.run(debug=True)