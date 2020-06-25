from pack.administradora import *


# stu1 = Student(name='Felix', email='felix@gmail.com', password='password1')
# stu2 = Student(name='Luis', email='luis@gmail.com', password='password2')
# stu3 = Student(name='Mario', email='mario@gmail.com', password='password3')
# stu4 = Student(name='Juan', email='juan@gmail.com', password='password4')
# stu5 = Student(name='Jose', email='jose@gmail.com', password='password5')
# stu1.save()
# stu2.save()
# stu3.save()
# stu4.save()
# stu5.save()

out = False
while not out:
    a = Admin()
    out = a.print_menu()
