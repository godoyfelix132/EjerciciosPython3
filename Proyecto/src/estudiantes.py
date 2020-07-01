class Student:
    __name = ''
    __mail = ''
    __password = ''

    def __init__(self, name='', mail='', password=''):
        self.__name = name
        self.__mail = mail
        self.__password = password

    def __str__(self):
        return 'Name: ' + self.__name + '\n' + 'Email: ' + self.__mail + '\n' + 'Password: ' + self.__password

    def set_name(self, name):
        self.__name = name

    def set_mail(self, mail):
        self.__mail = mail

    def set_password(self, password):
        self.__password = password

    def get_name(self):
        return self.__name

    def get_mail(self):
        return self.__mail

    def get_password(self):
        return self.__password
