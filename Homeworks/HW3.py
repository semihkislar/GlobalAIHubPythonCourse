students=[{'id':1},{'id':2},{'id':3},{'id':4},{'id':5}]

for i in students:
    i['name'] = input('Please input student name and surname: ')
    i['midterm'] = float(input('Please input student midterm point: '))
    i['project'] = float(input('Please input student project point: '))
    i['final'] = float(input('Please input student final point: '))
    i['grade'] = (i['midterm'] * 0.3) + (i['project'] * 0.3) + (i['final'] * 0.3)

newStudenList = sorted(students, key=lambda k: k['grade'], reverse=True)

for j in newStudenList:
    print(j)