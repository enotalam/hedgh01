
from csv import reader, writer

with open('students.csv',encoding='utf-8') as data_file:
    students_nom = list(reader(data_file,delimiter=','))
    head_lines = students_nom.pop(0)
students = list()

for i in students_nom:
    if '10' in i[3] and i[-1]!= 'None':
        students.append(i)

for i in range(1, len(students)):
    if int(students[i][-1]) > int(students[i-1][-1]):
        pos = i
        while pos != 0 and int(students[pos][-1]) > int(students[pos-1][-1]):
            item = students[pos]
            students[pos] = students[pos - 1]
            students[pos - 1] = item
            pos-=1

print('10 класс')
for i in range(3):
    full_name = students[i][1]
    full_name = full_name.split()
    name = full_name[1]
    second_name = full_name[0]
    print(f"{str(i + 1)} место: {name[0]}. {second_name}")