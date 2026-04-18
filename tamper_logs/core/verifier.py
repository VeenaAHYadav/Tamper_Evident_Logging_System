import json
from core.security import generate_hash, create_log_string
from config import LOG_FILE


def verify_logs():
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except Exception as e:
        return False, f"Error reading logs: {str(e)}"

    if not isinstance(logs, list) or len(logs) == 0:
        return False, "No logs found"

    for i, log in enumerate(logs):

        # -------------------------------
        # 1. DETECT DELETION / REORDERING (INDEX CHECK)
        # -------------------------------
        if log.get("index") != i:
            if log.get("index", -1) > i:
                return False, f"🚨 Log deletion detected at position {i}"
            else:
                return False, f"🚨 Log reordering detected at position {i}"

        # -------------------------------
        # 2. DETECT MODIFICATION (HASH CHECK)
        # -------------------------------
        try:
            data_string = create_log_string(log)
            recalculated_hash = generate_hash(data_string)
        except Exception as e:
            return False, f"Error processing log at index {i}: {str(e)}"

        if log.get("hash") != recalculated_hash:
            return False, f"🚨 Log modification detected at index {i}"

        # -------------------------------
        # 3. DETECT CHAIN BREAK (DELETION / REORDER)
        # -------------------------------
        if i > 0:
            if log.get("previous_hash") != logs[i - 1].get("hash"):
                return False, f"🚨 Chain broken at index {i} (possible deletion/reordering)"

        # -------------------------------
        # 4. GENESIS LOG CHECK
        # -------------------------------
        if i == 0:
            if log.get("previous_hash") != "0":
                return False, "🚨 First log corrupted"

    return True, "✅ Logs verified successfully"