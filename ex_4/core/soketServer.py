import socket
import json
from ex_4.storage.storage import Storage

class SocketServer():
    def __init__(self, HOST: str, PORT: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((HOST, PORT))
        self.storage = Storage()
        print(f"UDP server started on {HOST}:{PORT}")
        
    def start(self):
        try:
            while True:
                data, address = self.sock.recvfrom(1024)
                print("Recive data:", data)
                print("from:", address)
                self.sock.sendto(data, address)
                self.storage.write_to_file(json.loads(data))
        except KeyboardInterrupt:
            self.sock.close() 
                
            
    def close(self):
        print(f'UDP server destroyed')
        self.sock.close()