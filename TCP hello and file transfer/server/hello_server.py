import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received message: {message}")
    client_socket.send("Hello from server!".encode('utf-8'))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
