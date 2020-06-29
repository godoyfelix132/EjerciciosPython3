
from threading import Thread

import time

salir = [False, False, False]


def greeting(numero, nombre, fecha, lugar):
    while not salir[numero -1]:
        print(f'[{numero}] Hola {nombre}!\nFecha de nacimiento: {fecha}\nLugar de nacimineto: {lugar}')
        time.sleep(1)

    print(f'[{numero}] Saliendo ...')


def sleeper(i):
    print(f'Thread {i} sleeps for {i} seconds')
    time.sleep(i)
    print(f'Thread {i} woke up')


number = [1, 2, 3]
nombres = ['ana', 'maria', 'jose']
fechas = ['2000/02/23', '1952/08/12', '1997/12/07']
lugares = ['Jalisco', 'Colima', 'Nayarit']


for no, n, f, l in zip(number, nombres, fechas, lugares):
    t = Thread(target=greeting, args=(no, n, f, l))
    t.start()

for index, _ in enumerate(salir):
    time.sleep(5)
    salir[index] = True


# for j in range(10):
#     t = Thread(target=sleeper, args=(j,))
#     t.start()