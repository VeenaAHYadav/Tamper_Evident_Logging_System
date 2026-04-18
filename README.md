# Tamper_Evident_Logging_System
Tamper-evident logging system using HMAC-based hash chaining to detect log modification, deletion, and reordering with real-time verification and dashboard visualization.

This project implements a tamper-evident logging system designed to ensure the integrity and reliability of log data.
It uses cryptographic techniques to detect any unauthorized modification, deletion, or reordering of log entries.
The system simulates real-world audit logging mechanisms used in secure environments such as financial systems and cybersecurity monitoring.

🚀 Features
🔗 Hash chaining between log entries
🔐 HMAC-based secure hashing (SHA-256)
🛡️ Detection of:
Log modification
Log deletion
Log reordering
📊 Interactive dashboard (Streamlit)
🌐 API support (Flask)
⚡ Real-time log verification
🧠 How It Works

Each log entry contains:

Event details (timestamp, type, message, user)
Hash of the previous log
Its own cryptographic hash

This creates a chain of trust:

Log1 → Hash A  
Log2 → Previous Hash = A → Hash B  
Log3 → Previous Hash = B → Hash C  

Any change in earlier logs breaks the chain and is immediately detected.
