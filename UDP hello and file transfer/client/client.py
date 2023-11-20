import socket

def receive_file(filename, sock):
    with open(filename, 'wb') as file:
        while True:
            data, addr = sock.recvfrom(1024)
            if not data:
                break
            file.write(data)

    print(f"File '{filename}' received successfully.")

def start_client(filename, host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(b'file request', (host, port))
        receive_file(filename, sock)

if __name__ == "__main__":
    filename = input("Enter the name for the received file: ")
    start_client(filename)
