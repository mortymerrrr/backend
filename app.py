import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.txt"


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return jsonify({"status": "ok", "received": text}), 200


@app.route("/read", methods=["GET"])
def read_file():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""
    return jsonify({"status": "ok", "content": content})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)