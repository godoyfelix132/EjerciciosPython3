import socket as s


class ServerUtp:
    def __init__(self, ip='', port=12345):
        self.server_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.server_socket.bind((str(ip), int(port)))
        # self.server_socket.listen()
        print(f'Server created by port {port} and listening for connection')

    def read(self):
        message, address = self.server_socket.recvfrom(1024)
        return message.decode(), address

    def send(self, message, address):
        self.server_socket.sendto(message.encode(), address)

    def close_connection(self):
        self.server_socket.close()


server = ServerUtp('', 12345)

for i in range(10):
    message_received, from_address = server.read()
    print(f'Server - I received: {message_received}')
    message_to_send = f'I received: {message_received} from {from_address}'
    server.send(message_to_send, from_address)
    print(f'Server - Message sent: {message_to_send}')

print(f'Closing server')
server.close_connection()
print('Server closed')

