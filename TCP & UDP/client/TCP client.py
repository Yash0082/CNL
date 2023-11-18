import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 6006))

    operator = input("Enter operation (+, -, /, *): ")
    op1, op2 = map(int, input("Enter operands (op1 op2): ").split())

    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator. Supported operators are +, -, *, /")
        return

    client_socket.send(operator.encode('utf-8'))
    client_socket.send(op1.to_bytes(4, byteorder='big'))
    client_socket.send(op2.to_bytes(4, byteorder='big'))

    result = int.from_bytes(client_socket.recv(4), byteorder='big')
    print(f"Operation result from server: {result}")

    client_socket.close()

if __name__ == '__main__':
    main()
