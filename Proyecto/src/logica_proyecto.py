from src.estudiante import *
from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import Slot
from src.ui_proyecto import *
import pickle
import socket as s
import time


class ClientTcp:
    client = None

    def __init__(self, ip='127.0.0.1', port=35491):
        ip = str(ip)
        port = int(port)
        try:
            self.client = s.socket()
        except OSError as msg:
            self.client = None
            print(msg)
        try:
            self.client.connect((ip, port))
        except OSError as msg:
            self.client.close()
            self.client = None
            print(msg)

    def connection_state(self):
        if self.client == None:
            return False
        else:
            return True

    def send_student(self, message):
        self.client.send(message)

    def send_message(self, message):
        self.client.send(message.encode())

    def send_file(self, buffer):
        self.client.send(buffer)

    def receive(self):
        message = self.client.recv(1024)
        print(message)
        return message.decode()

    def close_connection(self):
        self.client.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_connect.clicked.connect(self.client_connect)
        self.ui.pushButton_send_student.clicked.connect(self.send_student)
        self.ui.pushButton_search.clicked.connect(self.open_file)
        self.ui.pushButton_send_file.clicked.connect(self.send_file)
        self.reset_connection()

    def send_file(self):
        filename = self.ui.lineEdit_file.text()
        self.client.send_message('iniciozip')
        file = open(filename, 'rb')
        i = file.read(500)
        count = 0
        while i:
            print(f'[{count + 1}:{len(i)}] {len(i)}')
            self.client.send_file(i)
            count += 1
            i = file.read(500)
        file.close()
        time.sleep(0.5)
        self.client.send_message('finzip')
        self.ui.label_state.setText('Archivo enviado')

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'Zip Files(*.zip)')
        print(filename[0])
        self.ui.lineEdit_file.setText(filename[0])

    def server_widgets(self, state):
        if state:
            self.ui.lineEdit_ip.setEnabled(True)
            self.ui.lineEdit_port.setEnabled(True)
        else:
            self.ui.lineEdit_ip.setEnabled(False)
            self.ui.lineEdit_port.setEnabled(False)

    def student_widgets(self, state):
        if state:
            self.ui.lineEdit_name.setEnabled(True)
            self.ui.lineEdit_email.setEnabled(True)
            self.ui.lineEdit_password.setEnabled(True)
            self.ui.pushButton_send_student.setEnabled(True)
        else:
            self.ui.lineEdit_name.setEnabled(False)
            self.ui.lineEdit_email.setEnabled(False)
            self.ui.lineEdit_password.setEnabled(False)
            self.ui.pushButton_send_student.setEnabled(False)

    def file_widgets(self, state):
        if state:
            self.ui.lineEdit_file.setEnabled(True)
            self.ui.pushButton_send_file.setEnabled(True)
            self.ui.pushButton_search.setEnabled(True)
        else:
            self.ui.lineEdit_file.setEnabled(False)
            self.ui.pushButton_send_file.setEnabled(False)
            self.ui.pushButton_search.setEnabled(False)

    def send_student(self):
        try:
            name = self.ui.lineEdit_name.text()
            email = self.ui.lineEdit_email.text()
            password = self.ui.lineEdit_password.text()
            student = Estudiante(name, email, password)
            student_bytes = pickle.dumps(student)
            print(student)
            self.client.send_student(student_bytes)
            message = (self.client.receive())
            print(message)
            if message == 'enviararchivo':
                self.file_widgets(1)
                self.student_widgets(0)
            else:
                self.ui.label_state.setText('servidor no envió enviararchivo')
        except:
            self.reset_connection()

    def reset_connection(self):
        try:
            self.client.close_connection()
        except:
            pass
        self.ui.label_state.setText('Desconectado')
        self.ui.pushButton_connect.setText('Conectar')
        self.ui.lineEdit_ip.setText('127.0.0.1')
        self.ui.lineEdit_port.setText('35491')
        self.file_widgets(0)
        self.student_widgets(0)
        self.server_widgets(1)

    def client_connect(self):
        self.server_widgets(0)
        self.ip = self.ui.lineEdit_ip.text()
        self.port = self.ui.lineEdit_port.text()
        if self.ui.pushButton_connect.text() == 'Conectar':
            self.client = ClientTcp(self.ip, self.port)
            if self.client.connection_state():
                self.ui.label_state.setText('Conectado')
                self.ui.pushButton_connect.setText('Desconectar')
                self.student_widgets(1)
            else:
                self.ui.label_state.setText('Error al conecta')
                self.reset_connection()
        else:
            self.reset_connection()


