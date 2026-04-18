from core.logger import add_log
from core.verifier import verify_logs

def main():
    add_log("LOGIN", "User logged in", "admin")
    add_log("FILE_ACCESS", "Opened file", "admin")

    status, msg = verify_logs()
    print(status, msg)

if __name__ == "__main__":
    main()