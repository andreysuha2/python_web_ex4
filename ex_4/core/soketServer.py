import socket

class SocketServer():
    def __init__(self, HOST: str, PORT: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((HOST, PORT))
        print(f"UDP server started on {HOST}:{PORT}")
        
    def start(self):
        while True:
            try: 
                data, address = self.sock.recv(1024)
                self.sock.sendto(data, address)
            except socket.timeout:
                continue
            except KeyboardInterrupt:
                print(f'UDP server destroyed')
            finally:
                self.sock.close()