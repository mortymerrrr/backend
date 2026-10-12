import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Директория данных берётся из окружения, по умолчанию — текущая (локальный запуск)
DATA_DIR = os.environ.get("DATA_DIR", ".")
DATA_FILE = os.path.join(DATA_DIR, "data.txt")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return jsonify({"status": "ok", "received": text}), 200


@app.route("/read", methods=["GET"])
def read():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""
    return jsonify({"content": content, "status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)