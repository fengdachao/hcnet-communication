import socket
import os

# HOST = "192.168.3.4"  # The server's hostname or IP address
HOST = "localhost"
PORT = 9001 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('./upload-images/img1.jpg', 'rb') as imageFile:
      contents = imageFile.read()
      # s.sendall(b"Hello, world")
      print('content:%s'%len(contents))
      s.sendall(contents)
      imageFile.close()
    data = s.recv(2048)

print(f"Received {data!r}")
s.close()