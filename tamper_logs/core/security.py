import hashlib
import json

def generate_hash(data_string):
    return hashlib.sha256(data_string.encode()).hexdigest()

def create_log_string(log):
    return json.dumps({
        "index": log["index"],
        "timestamp": log["timestamp"],
        "type": log["type"],
        "message": log["message"],
        "user": log["user"],
        "previous_hash": log["previous_hash"]
    }, sort_keys=True)