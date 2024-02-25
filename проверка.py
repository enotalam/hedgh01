
from csv import reader, writer

def hash(user):
    user= user.replace(' ','')
    hash_cod = 0
    letters = '_абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    p = 67
    m = 10**9 + 9
    for i in range(len(user)):
        s = letters.find(user[i])
        hash_cod = (hash_cod +s*(p**i)%m)%m
    return hash_cod

with open('students.csv',encoding='utf-8') as data_file:
    students = list(reader(data_file,delimiter=','))
    head_line = students.pop(0)

for i in range (len(students)):
    user_name = str(students[i][1])
    students[i][0] = hash(user_name)

with open('students_password2.csv', 'w', encoding='utf-8') as data_file:
    data_writer = writer(data_file, delimiter=',')
    data_writer.writerow(head_line)
    data_writer.writerows(students)