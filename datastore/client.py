import socket

HOST = "0.0.0.0"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while True:
        sock.sendall(input().encode())
        data = sock.recv(1024)

        print(data.decode("utf-8"))
