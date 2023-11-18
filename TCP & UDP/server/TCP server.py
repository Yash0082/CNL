import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 6006))
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        conn, addr = server_socket.accept()
        print("Connection from:", addr)

        operator = conn.recv(1).decode('utf-8')
        op1 = int.from_bytes(conn.recv(8), byteorder='big')
        op2 = int.from_bytes(conn.recv(8), byteorder='big')

        result = 0
        if operator == '+':
            result = op1 + op2
        elif operator == '-':
            result = op1 - op2
        elif operator == '*':
            result = op1 * op2
        elif operator == '/':
            result = op1 / op2
        else:
            print("Unsupported operation")

        conn.send(result.to_bytes(8, byteorder='big'))
        conn.close()

if __name__ == '__main__':
    main()
