import socket

# Define the server host and port
HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Get the filename from the user
    filename = input("Enter the filename to download: ")
    client_socket.sendto(filename.encode(), (HOST, PORT))

    received_data = b""
    while True:
        data, server_addr = client_socket.recvfrom(1024)
        if data == b"File not found":
            print(f"File '{filename}' not found on the server.")
            break
        received_data += data
        if len(data) < 1024:
            break

    with open(f"received_{filename}", 'wb') as file:
        file.write(received_data)
        print(f"File '{filename}' downloaded and saved as 'received_{filename}'")

if __name__ == '__main__':
    start_client()
