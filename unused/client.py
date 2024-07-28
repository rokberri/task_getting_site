# echo-client.py

import socket
from getpass import getuser

HOST = "100.93.86.9"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
current_user = str(getuser())
s.send(current_user.encode())
while True:
    user_info = str(input()) 
    s.send(user_info.encode())