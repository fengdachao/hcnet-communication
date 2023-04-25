import socket
import os

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9001 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with open('./images/hongye.png', 'rb') as imageFile:
      contents = imageFile.read()
      s.sendall(contents)
      print('content:%s'%len(contents))
      imageFile.close()
    s.sendall(b'client')
    data = s.recv(1024)
    s.close()

print(f"Received {data!r}")