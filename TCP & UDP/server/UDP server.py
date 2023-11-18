import socket

# Define the server host and port UDP Server
HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        filename = data.decode()
        print(f"Received request for file: {filename}")

        try:
            with open(filename, 'rb') as file:
                file_data = file.read(1024)
                while file_data:
                    server_socket.sendto(file_data, addr)
                    file_data = file.read(1024)
                print(f"File '{filename}' sent to {addr}")
        except FileNotFoundError:
            server_socket.sendto(b"File not found", addr)
            print(f"File '{filename}' not found")

if __name__ == '__main__':
    start_server()
