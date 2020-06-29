from src.estudiantes import *
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2.QtCore import Slot
from PySide2.QtGui import *
from src.forma import *
import re


class MainWindow(QMainWindow):
    __current_student_id = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_save.clicked.connect(self.save)
        self.ui.treeWidget_list.setHeaderLabels(['ID', 'NOMBRE'])
        self.ui.treeWidget_list.setAlternatingRowColors(True)
        self.ui.pushButton_delete.clicked.connect(self.delete)
        self.ui.pushButton_edit.clicked.connect(self.edit)
        self.ui.comboBox_del_mod.currentTextChanged.connect(self.show_info)
        self.update_widgets()


    def show_info(self):
        self.ui.textEdit_info.clear()
        s = (self.ui.comboBox_del_mod.currentText())
        r = re.match('[0-9]*', s)
        try:
            ix = (r.group(0))
            for s, i in zip(Student.objects, range(len(Student.objects))):
                if i == int(ix):
                    break
        except:
            pass
        self.ui.textEdit_info.append('Nombre:  ' + s.name)
        self.ui.textEdit_info.append('')
        self.ui.textEdit_info.append('Correo:  ' + s.email)
        self.ui.textEdit_info.append('')
        self.ui.textEdit_info.append('Contraseña:  ' + s.password)

    def delete(self):
        s = (self.ui.comboBox_del_mod.currentText())
        r = re.match('[0-9]+', s)
        ix = (r.group(0))
        for s, i in zip(Student.objects, range(len(Student.objects))):
            if i == int(ix):
                s.delete()
        self.update_widgets()
        self.ui.textEdit_info.clear()
        self.ui.textEdit_info.append('Se eliminó el estudiante correctamente...')

    def edit(self):
        s = (self.ui.comboBox_del_mod.currentText())
        r = re.match('[0-9]+', s)
        ix = (r.group(0))

        for s, i in zip(Student.objects, range(len(Student.objects))):
            if i == int(ix):
                self.__current_student_id = s.id
                break

        self.ui.lineEdit_name.setText(s.name)
        self.ui.lineEdit__email.setText(s.email)
        self.ui.lineEdit__password.setText(s.password)

        self.ui.pushButton_save.setText('Modificar')


    def update_widgets(self):
        self.ui.comboBox_del_mod.clear()
        self.ui.treeWidget_list.clear()

        self.ui.comboBox_del_mod.addItems(self.items_db())

        for s, i in zip(Student.objects, range(len(Student.objects))):
            top_data = [str(i), str(s.name)]
            sub_data = ['', 'Correo: ' + str(s.email) + '\t' + 'Contraseña: ' + str(s.password)]
            top = QTreeWidgetItem(top_data)
            QTreeWidgetItem(top, sub_data)
            self.ui.treeWidget_list.addTopLevelItem(top)

    @Slot()
    def save(self):
        button_name = self.ui.pushButton_save.text()
        if button_name == 'Guardar':
            # print(f'Name: {self.ui.lineEdit_name.text()}\nEmail: {self.ui.lineEdit__email.text()}\n'
            #       f'Password: {self.ui.lineEdit__password.text()}\n')
            name, email, password = self.ui.lineEdit_name.text(), self.ui.lineEdit__email.text(), self.ui.lineEdit__password.text()
            Student(name=name, email=email, password=password).save()
            self.ui.lineEdit_name.clear()
            self.ui.lineEdit__email.clear()
            self.ui.lineEdit__password.clear()
            self.update_widgets()
        elif button_name == 'Modificar':

            u = Student.objects(id=self.__current_student_id)\
                .update(name=self.ui.lineEdit_name.text(),
                        email=self.ui.lineEdit__email.text(), password=self.ui.lineEdit__password.text())
            self.ui.lineEdit_name.clear()
            self.ui.lineEdit__email.clear()
            self.ui.lineEdit__password.clear()
            self.ui.pushButton_save.setText('Guardar')
            self.ui.textEdit_info.clear()
            self.ui.textEdit_info.append('Se modificó el estudiante correctamente...')
            self.update_widgets()


    @staticmethod
    def items_db():
        dict_db_students = []
        for s, i in zip(Student.objects, range(len(Student.objects))):
            a = f'{i} - {s.name}'
            dict_db_students.append(a)
        return dict_db_students

    @staticmethod
    def items_details_db():
        dict_db_students = []
        for s, i in zip(Student.objects, range(len(Student.objects))):
            a = f'{i} - {s.name}'
            dict_db_students.append(a)
        return dict_db_students


if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()
