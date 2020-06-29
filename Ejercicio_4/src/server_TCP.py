import socket as s
import time


class ServerTcp:
    def __init__(self, ip='', port=35491):
        self.server_socket = s.socket()
        # self.server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        self.server_socket.bind((str(ip), int(port)))
        self.server_socket.listen()
        print(f'Server created by port {port} and listening for connection')
        (self.client_connection, self.client_address) = self.server_socket.accept()
        print(f'Connection successful with {self.client_address}')

    def read(self):
        message = self.client_connection.recv(1024)
        if not message:
            print(f'Closing connection with {self.client_connection.getsockname()}')
            self.client_connection.close()
            print('Connection closed')
            return False
        return message.decode()

    def send(self, message):
        self.client_connection.send(message.encode())

    def close_connection(self):
        self.client_connection.close()

    def get_address(self):
        return self.client_address


server = ServerTcp('', 35491)
while True:
    message_received = server.read()
    if message_received:
        print('Server - Message received: ' + str(message_received))
    else:
        break
    message_to_send = f'I received: {message_received}'
    server.send(message_to_send)
    print(f'Server - Message sent: {message_to_send}')

print(f'Closing server')
server.close_connection()
print('Server closed')
