import socket
import os

HOST = "192.168.3.2"  # The server's hostname or IP address
# HOST = "localhost"
PORT = 9001 # The port used by the server

def sendPic(fileName, port = PORT):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      print ('host:', HOST, port)
      s.connect((HOST, port))
      with open(fileName, 'rb') as imageFile:
        contents = imageFile.read()
        # s.sendall(b"Hello, world")
        print('content:%s'%len(contents))
        s.sendall(contents)
        imageFile.close()
      data = s.recv(2048)

  print(f"Received {data!r}")
  s.close()

def sendPicData(buf, port = PORT):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, port))
      s.sendall(buf)
      data = s.recv(2048)

  print(f"Received {data!r}")
  s.close()


if __name__ == '__main__':
  sendPic('./upload-images/img1.jpg')
