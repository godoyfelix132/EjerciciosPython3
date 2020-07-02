import socket
import time
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 35491)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            student = connection.recv(500)
            print('received {!r}'.format(student))
            if student:
                print('sending data back to the client')
                data = 'enviararchivo'
                connection.sendall(data.encode())

                init_zip = connection.recv(500)
                print(init_zip)
                if init_zip == b'iniciozip':
                    file = open('copia.zip', 'wb')
                    i = connection.recv(500)
                    count = 0
                    while i != b'finzip':
                        print(f'[{count + 1}:{len(i)}] {len(i)}')
                        file.write(i)
                        count += 1
                        i = connection.recv(500)
                        print(i)
                    time.sleep(0.5)
                    print('done')
                    file.close()
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()

