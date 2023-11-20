import socket

def send_file(filename, sock, addr):
    with open(filename, 'rb') as file:
        data = file.read()
        sock.sendto(data, addr)
        print(f"File '{filename}' sent to {addr} successfully.")

def start_server(filename, host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print(f'Server started at {host} on port {port}')
        while True:
            data, addr = sock.recvfrom(1024)
            if data:
                print('Received request from', addr)
                send_file(filename, sock, addr)

if __name__ == "__main__":
    filename = input("Enter the name of the file to transfer: ")
    start_server(filename)
