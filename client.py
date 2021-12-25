from binascii import unhexlify
import socket
import struct
import sys
from pycodecs import extcodec8, codec8

PROTOCOL = extcodec8

if len(sys.argv)==2 and sys.argv[1]=='codec8':
    PROTOCOL = codec8    

SERVER = "127.0.0.1"
PORT = 8080

if PROTOCOL == extcodec8:
  with open('data/extcodec8.hex', 'r') as f:
      data = f.read()
else:
  with open('data/codec8_3.hex', 'r') as f:
      data = f.read()

buffer = bytes()
for i in range(0,len(data),2):
    buffer += struct.pack('B', int(data[i:i+2],16))
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    client.sendall(buffer)
    while True:
      in_data =  client.recv(4)
      print("Response :" ,int(in_data[0:4].hex(), 16))
      break
except Exception as e:
    print(e)
    print("Exitting codec client ...")
finally:
    client.close()
