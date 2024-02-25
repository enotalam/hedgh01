
from csv import reader, writer

with open('students.csv',encoding='utf-8') as data_file:
    students = list(reader(data_file,delimiter=','))
    head_lines = students.pop(0)

id_pupil = input('Введите айди или стоп ')

while id_pupil != 'STOP':
    position = 1
    for pupil in students:
        if pupil[2] == id_pupil:
            pupil_name = pupil[1].split()
            grade = pupil[-1]
            position = 0
    if position ==0:
        print(f'Проект номер {id_pupil} делал {pupil_name[1][0]}. {pupil_name[0]} он получил{grade}')
    if position==1 :
        print('no')
    id_pupil = input('Введите айди или стоп ')