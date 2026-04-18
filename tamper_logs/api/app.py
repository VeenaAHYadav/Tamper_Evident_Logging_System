from flask import Flask, request, jsonify
from tamper_logs.core.logger import Logger
from tamper_logs.core.verifier import verify_logs

app = Flask(__name__)
logger = Logger()

@app.route("/log", methods=["POST"])
def add_log():
    data = request.json
    logger.add_log(data["type"], data["message"], data.get("user", "SYSTEM"))
    return jsonify({"status": "logged"})

@app.route("/verify")
def verify():
    status, msg = verify_logs()
    return jsonify({"status": status, "message": msg})

@app.route("/logs")
def get_logs():
    return jsonify(logger.logs)

if __name__ == "__main__":
    app.run(port=5001)