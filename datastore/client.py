import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while True:
        sock.sendall(input().encode())
        data = sock.recv(1024)

        print(data.decode('utf-8'))
