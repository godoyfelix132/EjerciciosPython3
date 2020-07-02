import socket as s
from threading import Thread
import time
import pickle


class ClientThread(Thread):
    def __init__(self, connection, address):
        Thread.__init__(self)
        self.__connection = connection
        self.__address = address

    def run(self):
        while True:
            try:
                student = self.read_student()
                if not student:
                    print(f'Closing connection with {self.__connection.getsockname()}')
                    self.__connection.close()
                    print('Connection closed')
                    return False
                print(f'Server - I received:')
                print(type(student))
                print(student)
                # a = input()
            except:
                self.__connection.close()
            message_to_send = 'enviararchivo'
            self.send(message_to_send)
            print(f'Server - I sent: {message_to_send}')
            self.read_file()

    def read_file(self):
        init_zip = self.__connection.recv(500)
        print(init_zip)
        if init_zip == b'iniciozip':
            file = open('copia.zip', 'wb')
            i = self.__connection.recv(500)
            count = 0
            while i != b'finzip':
                file.write(i)
                print(f'[{count + 1}:{len(i)}] {len(i)}')
                count += 1
                i = self.__connection.recv(500)
            time.sleep(1)
            end_zip = self.__connection.recv(500)
            print(end_zip)
            if init_zip == b'finzip':
                self.__connection.close()
                print('Connection closed')
            else:
                print(f'no coincide finzip con {end_zip}')
        else:
            print(f'iniciozip no coincide con {init_zip}')




    def read_student(self):
        try:
            message = self.__connection.recv(1024)
            student = pickle.loads(message)
            return student
        except:
            self.__connection.close()

    def send(self, message):
        try:
            self.__connection.send(message.encode())
        except:
            self.__connection.close()

class ServerTcp:
    def __init__(self, ip='', port=35491):
        self.server_socket = s.socket()
        # self.server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        self.server_socket.bind((str(ip), int(port)))
        print(type(port))
        self.server_socket.listen(5)
        print(f'Server created by port {port}')
        while True:
            self.client_connection, self.client_address = self.server_socket.accept()

            print(f'Connection successful with {self.client_address}')
            thread = ClientThread(self.client_connection, self.client_address)
            thread.start()
            time.sleep(0.5)


server = ServerTcp('', 35491)
