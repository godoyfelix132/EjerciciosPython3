from pack.estudiantes import *
from pack.StudenIO import *


stu1 = Student('Felix', 'felix@gmail.com', 'password1')
stu2 = Student('Luis', 'luis@gmail.com', 'password2')
stu3 = Student('Mario', 'mario@gmail.com', 'password3')
stu4 = Student('Juan', 'juan@gmail.com', 'password4')
stu5 = Student('Jose', 'jose@gmail.com', 'password5')

# WORKING WITH PICKLE

# Updating list of students
list_students = [stu1, stu2, stu3]
update_students_pickle(list_students)

# Saving students
save_students_pickle(stu4)
save_students_pickle(stu5)

# Reading students
list_students = read_students_pickle()
print('LIST WITH PICKLE')
for x in range(len(list_students)):
    print()
    print(list_students[x])


# WORKING WITH SHELVE

# Updating list of students
list_students_shelve = [stu1,stu2,stu3]
update_students_shelve(list_students_shelve)

# Saving student
save_students_shelve(stu4)
save_students_shelve(stu5)

# Reading students
list_students_shelve = read_students_shelve()
print('LIST WITH SHELVE')
for x in range(len(list_students_shelve)):
    print()
    print(list_students_shelve[x])

