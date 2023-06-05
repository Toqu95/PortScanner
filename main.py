import sys
import socket
import datetime
import threading

def checkport(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        print(f"Port {port} is open")
        count += 1
        return True
    except:
        return False

if __name__ == "__main__":
    ip = str(sys.argv[1])
    print("-" * 50)
    print(f"IP: {ip}")
    print("-" * 50)
    print(f"Date: {datetime.datetime.now()}")
    print("-" * 50)
    for port in range(1, 65535):
        threading.Thread(target=checkport, args=(ip, port)).start()
    print("-" * 50)
