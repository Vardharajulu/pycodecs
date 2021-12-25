import socket
import json
import sys
from pycodecs import extcodec8, codec8

PROTOCOL = extcodec8

if len(sys.argv)==2 and sys.argv[1]=='codec8':
    PROTOCOL = codec8    

def start_server():
    try:
        hostname, port = "127.0.0.1", 8080
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((hostname, port))
        server.listen(1)
        if PROTOCOL == extcodec8:
            print("AVL Codec 8 extended Server started ...")
        else:
            print("AVL Codec 8 Server started ...")
        return server
    except Exception as e:
        print("Failed to start AVL codec server")
        print(e)

def run_server(server):
    try:
        while True:
            print("Waiting for connection request ..")
            clientConnection,clientAddress = server.accept()
            print("Client Connected: " , clientAddress)
            print('listening to client ...')
            header = clientConnection.recv(8)
            data_length =  PROTOCOL.verify_header(header)
            crc_length = 4
            body_length = data_length + crc_length
            if data_length:
                data = clientConnection.recv(body_length)
                result = PROTOCOL.process_data(data, body_length)
                print(json.dumps(result,sort_keys=True, indent=4))
                PROTOCOL.send_response(clientConnection, result['records_count'])
            else:
                print("Header with Error/No Data")
                print("Client disconnected....")
                clientConnection.close()
    except Exception as e:
        print("Exitting codec server ...")
        
if __name__ == "__main__":
    server = start_server()
    if server:
        run_server(server)
