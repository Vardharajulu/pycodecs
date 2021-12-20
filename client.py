from binascii import unhexlify
import socket
import struct
SERVER = "127.0.0.1"
PORT = 8080

with open('data/extcodec8.hex', 'r') as f:
    data = f.read()

buffer = bytes()
for i in range(0,len(data),2):
    buffer += struct.pack('B', int(data[i:i+2],16))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(buffer)
while True:
  in_data =  client.recv(4)
  print("Response :" ,int(in_data[0:4].hex(), 16))
  break
client.close()
