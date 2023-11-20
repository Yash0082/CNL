import socket

def receive_file(filename, conn):
    with open(filename, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
        print("Received file:", filename)

def start_client(host='localhost', port=12345):
    filename = input("Enter the name for the received file: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        receive_file(filename, s)

if __name__ == "__main__":
    start_client()
