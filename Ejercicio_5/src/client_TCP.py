import socket as s
import time


class ClientTcp:
    def __init__(self, ip='127.0.0.1', port=35491):
        self.client = s.socket()
        self.client.connect((str(ip), int(port)))
        print(f'Connected with server')

    def send(self, message):
        self.client.send(message.encode())

    def receive(self):
        message = self.client.recv(1024)
        return message.decode()

    def close_connection(self):
        self.client.close()


client = ClientTcp()

for i in range(3):
    message_to_send = 'message_' + str(i)
    client.send(message_to_send)
    print(f'Client_2 - Message sent: {message_to_send}')
    print(f'Client_2 - Message received: {client.receive()}')
    # time.sleep(2)
    a = input()
client.close_connection()
