import socket as s
import time


class ClientUtp:
    def __init__(self, ip='127.0.0.1', port=12345):
        self.client = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.__ip = ip
        self.__port = port
        print(f'Socket created')

    def send(self, message):
        self.client.sendto(message.encode(), (self.__ip, self.__port))

    def receive(self):
        message, address = self.client.recvfrom(1024)
        return message.decode(), address

    def close_connection(self):
        self.client.close()


client = ClientUtp()

for i in range(10):
    message_to_send = 'message_' + str(i)
    client.send(message_to_send)
    print(f'Client - Message sent: {message_to_send}')
    message_received, from_address = client.receive()
    print(f'Client - Message received: {message_received} from: {from_address}')
    time.sleep(0.5)

client.close_connection()
