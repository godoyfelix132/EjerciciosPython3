import pickle
import shelve


# WORKING WITH PICKLE


def update_students_pickle(students):
    file = open('students_p.db', 'wb')
    for i in range(0, len(students)):
        pickle.dump(students[i], file, 4)
    file.close()


def save_students_pickle(student):
    file = open('students_p.db', 'ab')
    pickle.dump(student, file, 4)
    file.close()


def read_students_pickle():
    file = open('students_p.db', 'rb')
    a = pickle.Unpickler(file)
    students = []
    while True:
        try:
            o = a.load()
        except EOFError:
            break
        students.append(o)
    file.close()
    return students


# WORKING WITH SHELVE


def update_students_shelve(students):
    with shelve.open('students_s.db') as db:
        for i in range(len(students)):
            db[students[i].get_name()] = students[i]


def save_students_shelve(student):
    with shelve.open('students_s.db') as db:
        db[student.get_name()] = student


def read_students_shelve():
    with shelve.open('students_s.db') as db:
        keys = list(db.keys())
        db_list = []
        for i in range(len(keys)):
            db_list.append(db[keys[i]])
        return db_list
