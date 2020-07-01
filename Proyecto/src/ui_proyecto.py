# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forma.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(389, 457)
        MainWindow.setBaseSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_server = QGroupBox(self.centralwidget)
        self.groupBox_server.setObjectName(u"groupBox_server")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_server)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_server = QWidget(self.groupBox_server)
        self.widget_server.setObjectName(u"widget_server")
        self.horizontalLayout = QHBoxLayout(self.widget_server)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_ip = QLabel(self.widget_server)
        self.label_ip.setObjectName(u"label_ip")

        self.horizontalLayout.addWidget(self.label_ip)

        self.lineEdit_ip = QLineEdit(self.widget_server)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")

        self.horizontalLayout.addWidget(self.lineEdit_ip)

        self.label_port = QLabel(self.widget_server)
        self.label_port.setObjectName(u"label_port")

        self.horizontalLayout.addWidget(self.label_port)

        self.lineEdit_port = QLineEdit(self.widget_server)
        self.lineEdit_port.setObjectName(u"lineEdit_port")

        self.horizontalLayout.addWidget(self.lineEdit_port)


        self.verticalLayout_2.addWidget(self.widget_server)

        self.pushButton_connect = QPushButton(self.groupBox_server)
        self.pushButton_connect.setObjectName(u"pushButton_connect")

        self.verticalLayout_2.addWidget(self.pushButton_connect)

        self.label_connection = QLabel(self.groupBox_server)
        self.label_connection.setObjectName(u"label_connection")
        self.label_connection.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_connection)


        self.verticalLayout.addWidget(self.groupBox_server)

        self.groupBox_student = QGroupBox(self.centralwidget)
        self.groupBox_student.setObjectName(u"groupBox_student")
        self.formLayout_2 = QFormLayout(self.groupBox_student)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_name = QLabel(self.groupBox_student)
        self.label_name.setObjectName(u"label_name")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_name)

        self.lineEdit_name = QLineEdit(self.groupBox_student)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_email = QLabel(self.groupBox_student)
        self.label_email.setObjectName(u"label_email")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(self.groupBox_student)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_email)

        self.label_password = QLabel(self.groupBox_student)
        self.label_password.setObjectName(u"label_password")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_password)

        self.lineEdit_password = QLineEdit(self.groupBox_student)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_password)

        self.pushButton_send_student = QPushButton(self.groupBox_student)
        self.pushButton_send_student.setObjectName(u"pushButton_send_student")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.pushButton_send_student)


        self.verticalLayout.addWidget(self.groupBox_student)

        self.groupBox_file = QGroupBox(self.centralwidget)
        self.groupBox_file.setObjectName(u"groupBox_file")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_file)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_search_file = QWidget(self.groupBox_file)
        self.widget_search_file.setObjectName(u"widget_search_file")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_search_file)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_search = QPushButton(self.widget_search_file)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.horizontalLayout_2.addWidget(self.pushButton_search)

        self.lineEdit_file = QLineEdit(self.widget_search_file)
        self.lineEdit_file.setObjectName(u"lineEdit_file")

        self.horizontalLayout_2.addWidget(self.lineEdit_file)


        self.verticalLayout_3.addWidget(self.widget_search_file)

        self.pushButton_send_file = QPushButton(self.groupBox_file)
        self.pushButton_send_file.setObjectName(u"pushButton_send_file")

        self.verticalLayout_3.addWidget(self.pushButton_send_file)

        self.widget_state = QWidget(self.groupBox_file)
        self.widget_state.setObjectName(u"widget_state")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_state)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_state)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_state = QLabel(self.widget_state)
        self.label_state.setObjectName(u"label_state")
        self.label_state.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_state)


        self.verticalLayout_3.addWidget(self.widget_state)


        self.verticalLayout.addWidget(self.groupBox_file)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 389, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cliente F\u00e9lix Godoy Mart\u00ednez", None))
        self.groupBox_server.setTitle(QCoreApplication.translate("MainWindow", u"Servidor", None))
        self.label_ip.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.label_port.setText(QCoreApplication.translate("MainWindow", u"Puerto:", None))
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label_connection.setText("")
        self.groupBox_student.setTitle(QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton_send_student.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.groupBox_file.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_send_file.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Estado: ", None))
        self.label_state.setText("")
    # retranslateUi

