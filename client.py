import socket
import os

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9001 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('./images/hongye.png', 'rb') as imageFile:
      contents = imageFile.read()
      # s.sendall(b"Hello, world")
      print('content:%s'%len(contents))
      s.sendall(contents)
      imageFile.close()
    data = s.recv(1024)

print(f"Received {data!r}")
s.close()