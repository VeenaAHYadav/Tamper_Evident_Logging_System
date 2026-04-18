# 🔐 Tamper-Evident Logging System

## 📌 Overview

This project implements a **tamper-evident logging system** that ensures the integrity of log data.  
The system is designed so that once a log entry is created, it cannot be modified, deleted, or rearranged without being detected.

It uses cryptographic techniques similar to those used in real-world audit logging systems in cybersecurity and financial applications.

---

## 🚀 Features

- 🔗 Cryptographic hash chaining between logs  
- 🔐 HMAC-based hashing (SHA-256) for secure log generation  
- 🛡️ Detection of:
  - Log modification  
  - Log deletion  
  - Log reordering  
- 📊 Interactive dashboard using Streamlit  
- 🌐 API support using Flask  
- ⚡ Real-time log verification  

---

## 🧠 How It Works

Each log entry contains:
- Index  
- Timestamp  
- Event type  
- Message  
- User  
- Previous hash  
- Current hash  

Each log is linked to the previous one:
Log1 → Hash A
Log2 → Previous Hash = A → Hash B
Log3 → Previous Hash = B → Hash C


If any log is changed, removed, or reordered, the chain breaks and the system detects the tampering.

---

## 🏗️ Project Structure
```text
tamper_logs/
│
├── tamper_logs/
│   │
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── logger.py        # Handles log creation and chaining
│   │   ├── verifier.py      # Verifies integrity and detects tampering
│   │   ├── security.py      # HMAC hash generation
│   │   ├── storage.py       # Read/write logs
│   │
│   ├── dashboard/
│   │   ├── __init__.py
│   │   └── dashboard.py     # Streamlit dashboard UI
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── app.py           # Flask API
│
├── data/
│   └── logs.json            # Stored log entries
│
├── README.md

```
---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tamper_logs.git
cd tamper-logs
```

### 2. Install dependencies
```bash
pip install streamlit flask
```

### 3. Run the system
```bash
python -m tamper_logs.main
```
### 4. Launch dashboard
```bash
streamlit run tamper_logs/dashboard/dashboard.py
```


👤 Author

VEENA AH

