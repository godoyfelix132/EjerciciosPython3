from mongoengine import *

connect('students')

class Student(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)

    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'Email: ' + self.email + '\n' + 'Password: ' + self.password

    def set_name(self, name):
        self.name = name

    def set_mail(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name

    def get_mail(self):
        return self.email

    def get_password(self):
        return self.password
