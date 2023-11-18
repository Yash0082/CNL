import socket

def send_file(filename, conn):
    with open(filename, 'rb') as file:
        conn.sendall(file.read())

def start_server(host = 'localhost', port = 12345):
    filename = input("Enter the name of the file to transfer: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            send_file(filename, conn)

if __name__ == "__main__":
    start_server()
