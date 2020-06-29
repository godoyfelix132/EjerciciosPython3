import threading

import time


class Hi(threading.Thread):
    name = ''
    inc = 0
    n = 0

    def __init__(self, number, name, seconds):
        threading.Thread.__init__(self)
        self.name = name
        self.inc = number
        self.seconds = seconds

    def run(self):
        for i in range(3):
            # print(f'hola {self.name}')
            time.sleep(self.seconds)


if __name__ == '__main__':
    h1 = Hi(1, 'felix', 1)
    h1.start()
    print(h1.ident)
    h2 = Hi(1, 'joel', 0.5)
    h2.start()
    time.sleep(1)
    print(h1.ident)
    print(h2.ident)
    print(threading.active_count())
