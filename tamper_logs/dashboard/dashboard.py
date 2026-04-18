import streamlit as st
import json
import os
import sys

# Fix path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.logger import add_log
from core.verifier import verify_logs
from config import LOG_FILE

st.set_page_config(page_title="Tamper-Proof Logs", layout="wide")
st.title("🛡️ Tamper-Proof Logging Dashboard")

def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

logs = load_logs()

# Sidebar
st.sidebar.header("Add Log")
log_type = st.sidebar.selectbox("Type", ["LOGIN", "FILE_ACCESS", "ERROR"])
message = st.sidebar.text_input("Message", "User action")
user = st.sidebar.text_input("User", "admin")

if st.sidebar.button("Add Log"):
    add_log(log_type, message, user)
    st.rerun()

# Verify
status, msg = verify_logs()
if status:
    st.success(msg)
else:
    st.error(msg)

# Show logs
st.subheader("Logs")
st.dataframe(logs, use_container_width=True)

# Attack simulation
st.subheader("Simulate Attack")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Modify"):
        if logs:
            logs[0]["message"] = "HACKED"
            with open(LOG_FILE, "w") as f:
                json.dump(logs, f, indent=4)
            st.rerun()

with col2:
    if st.button("Delete"):
        if logs:
            logs.pop(0)
            with open(LOG_FILE, "w") as f:
                json.dump(logs, f, indent=4)
            st.rerun()

with col3:
    if st.button("Reorder"):
        if len(logs) > 1:
            logs[0], logs[1] = logs[1], logs[0]
            with open(LOG_FILE, "w") as f:
                json.dump(logs, f, indent=4)
            st.rerun()