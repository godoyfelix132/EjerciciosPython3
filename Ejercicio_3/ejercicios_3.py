from pack.figuras import *
from pack.estudiantes import *


def print_object(object):
    print(object, 'Is type:', object.get_type())


fig1 = Figure(color='Black')
fig1.set_area(40)
fig1.set_perimeter(20)
print_object(fig1)

rec1 = Rectangle(color='blue', high=10,  width=20)
rec1.set_area(30)
rec1.set_perimeter(40)
print_object(rec1)

tri1 = Triangle(color='yellow', side1=1, side2=5, side3=10)
tri1.set_area(20)
tri1.set_perimeter(5)
print_object(tri1)

stu1 = Student(name='Felix', mail='godoyfelix132@gmail.com', password='password')
print(stu1)
stu1.set_name('Luis')
stu1.set_mail('luis@gmail.com')
stu1.set_password('Second_password')
print('The name is', stu1.get_name())
print('The email is', stu1.get_mail())
print('The password is', stu1.get_password())
