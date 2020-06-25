from pack.estudiantes import *


class Admin:
    def print_menu(self):
        print('1 - Write new student')
        print('2 - Read student')
        print('3 - Update student')
        print('4 - Delete student')
        print('5 - Exit')
        opc = int(input())
        if opc == 1:
            self.write()
        elif opc == 2:
            s = self.read()
            print(s)
        elif opc == 3:
            s = self.update()
            print(s)
        elif opc == 4:
            obj = self.delete()
            print(obj)
        elif opc == 5:
            return True
        else:
            print('incorrect option')

    @staticmethod
    def get_info():
        name = input('Name: ')
        email = input('Email: ')
        password = input('Password: ')
        return name, email, password

    def write(self):
        name, email, password = self.get_info()
        Student(name=name, email=email, password=password).save()

    @staticmethod
    def read():
        dict_db_students = {}
        for s, i in zip(Student.objects, range(len(Student.objects))):
            print(f'{i} - {s.name}')
            dict_db_students[i] = s.id
        print(dict_db_students)
        i = int(input())
        s = Student.objects.get(id=dict_db_students[i])
        return s

    def update(self):
        dict_db_students = {}
        for s, i in zip(Student.objects, range(len(Student.objects))):
            print(f'{i} - {s.name}')
            dict_db_students[i] = s.id
        i = int(input())
        name, email, password = self.get_info()
        u = Student.objects(id=dict_db_students[i]).update(name=name, email=email, password=password)
        if u:
            s = Student.objects.get(id=dict_db_students[i])
            return s
        else:
            print('Error')

    @staticmethod
    def delete():
        dict_db_students = {}
        for s, i in zip(Student.objects, range(len(Student.objects))):
            print(f'{i} - {s.name}')
            dict_db_students[i] = s.id
        i = int(input())
        u = Student.objects(id=dict_db_students[i]).delete()
        if u:
            list_students = []
            for s in Student.objects:
                list_students.append(s)
            return list_students
        else:
            print('Error')
