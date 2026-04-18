import json
import os
from datetime import datetime
from core.security import generate_hash, create_log_string
from config import LOG_FILE

def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

def add_log(log_type, message, user):
    logs = load_logs()

    index = len(logs)
    previous_hash = logs[-1]["hash"] if logs else "0"

    new_log = {
        "index": index,
        "timestamp": datetime.now().isoformat(),
        "type": log_type,
        "message": message,
        "user": user,
        "previous_hash": previous_hash
    }

    data_string = create_log_string(new_log)
    new_log["hash"] = generate_hash(data_string)

    logs.append(new_log)
    save_logs(logs)

    return new_log