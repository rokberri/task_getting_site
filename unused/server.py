# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print(f"Connected by {addr}")

curr_user = conn.recv(1024)
curr_user = curr_user.decode()
print(str(curr_user))

while True:
    command = conn.recv(1024)
    command = command.decode()
    print(command)
    if command == 'exit':
        break
