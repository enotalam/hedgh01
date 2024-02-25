from random import shuffle, sample
from csv import reader, writer

def login(pupil):
    pupil = pupil.split()
    login = pupil[0]+'_'+pupil[1][0]+pupil[2][0]
    return login
def password():
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    number = '1234567890'
    password_pupil = sample(letters.upper(),1)
    password_pupil += sample(letters, 1)
    password_pupil += sample(number, 6)
    shuffle(password_pupil)
    return ''.join(password_pupil)

with open('students.csv',encoding='utf-8') as data_file:
    students = list(reader(data_file,delimiter=','))
    head_line = students.pop(0)

for pupil in students:
    pupil.append(login(pupil[1]))
    pupil.append(password())

with open('students_login.csv','w', encoding='utf-8') as data_file:
    students_writer = writer(data_file,delimiter=',')
    head_line.append('login')
    head_line.append('password')
    students_writer.writerow(head_line)
    students_writer.writerows(students)