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
        MainWindow.resize(469, 682)
        MainWindow.setBaseSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.lineEdit__email = QLineEdit(self.groupBox_student)
        self.lineEdit__email.setObjectName(u"lineEdit__email")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit__email)

        self.label_password = QLabel(self.groupBox_student)
        self.label_password.setObjectName(u"label_password")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_password)

        self.lineEdit__password = QLineEdit(self.groupBox_student)
        self.lineEdit__password.setObjectName(u"lineEdit__password")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit__password)

        self.pushButton_save = QPushButton(self.groupBox_student)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.pushButton_save)


        self.verticalLayout.addWidget(self.groupBox_student)

        self.groupBox_del_mod = QGroupBox(self.centralwidget)
        self.groupBox_del_mod.setObjectName(u"groupBox_del_mod")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_del_mod)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_del_mod = QComboBox(self.groupBox_del_mod)
        self.comboBox_del_mod.setObjectName(u"comboBox_del_mod")

        self.horizontalLayout_3.addWidget(self.comboBox_del_mod)

        self.widget_del_mod = QWidget(self.groupBox_del_mod)
        self.widget_del_mod.setObjectName(u"widget_del_mod")
        self.verticalLayout_3 = QVBoxLayout(self.widget_del_mod)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_delete = QPushButton(self.widget_del_mod)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.verticalLayout_3.addWidget(self.pushButton_delete)

        self.pushButton_edit = QPushButton(self.widget_del_mod)
        self.pushButton_edit.setObjectName(u"pushButton_edit")

        self.verticalLayout_3.addWidget(self.pushButton_edit)


        self.horizontalLayout_3.addWidget(self.widget_del_mod)


        self.verticalLayout.addWidget(self.groupBox_del_mod)

        self.groupBox_info = QGroupBox(self.centralwidget)
        self.groupBox_info.setObjectName(u"groupBox_info")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit_info = QTextEdit(self.groupBox_info)
        self.textEdit_info.setObjectName(u"textEdit_info")

        self.verticalLayout_2.addWidget(self.textEdit_info)


        self.verticalLayout.addWidget(self.groupBox_info)

        self.groupBox_list = QGroupBox(self.centralwidget)
        self.groupBox_list.setObjectName(u"groupBox_list")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_list)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.treeWidget_list = QTreeWidget(self.groupBox_list)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_list.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_list.setObjectName(u"treeWidget_list")
        self.treeWidget_list.setMinimumSize(QSize(0, 200))

        self.verticalLayout_4.addWidget(self.treeWidget_list)


        self.verticalLayout.addWidget(self.groupBox_list)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Estudiantes", None))
        self.groupBox_student.setTitle(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.groupBox_del_mod.setTitle(QCoreApplication.translate("MainWindow", u"Eliminar / modificar", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.groupBox_info.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.groupBox_list.setTitle(QCoreApplication.translate("MainWindow", u"Lista de estudiantes", None))
    # retranslateUi

