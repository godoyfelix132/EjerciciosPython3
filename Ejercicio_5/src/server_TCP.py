import socket as s
from threading import Thread
import time


class ClientThread(Thread):
    def __init__(self, connection, address):
        Thread.__init__(self)
        self.__connection = connection
        self.__address = address

    def run(self):
        while True:
            message_received = self.read()
            if not message_received:
                print(f'Closing connection with {self.__connection.getsockname()}')
                self.__connection.close()
                print('Connection closed')
                return False
            print(f'Server - I received: {message_received}  from {self.__address}')
            message_to_send = f'I received: {message_received}'
            self.send(message_to_send)
            print(f'Server - I sent: {message_to_send}')

    def read(self):
        message = self.__connection.recv(1024)
        return message.decode()

    def send(self, message):
        self.__connection.send(message.encode())


class ServerTcp:
    def __init__(self, ip='', port=35491):
        self.server_socket = s.socket()
        # self.server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        self.server_socket.bind((str(ip), int(port)))
        self.server_socket.listen(5)
        print(f'Server created by port {port}')
        while True:
            self.client_connection, self.client_address = self.server_socket.accept()
            print(f'Connection successful with {self.client_address}')
            thread = ClientThread(self.client_connection, self.client_address)
            thread.start()
            time.sleep(0.5)


server = ServerTcp('', 35491)

