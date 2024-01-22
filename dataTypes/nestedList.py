#archivo = open("input.txt")

##print(archivo.read())

#input = archivo.read()


if __name__ == '__main__':
    
    students_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_data.append([name, score])

students_data.sort(key=lambda x : (x[1], x[0]))

print(students_data)

second_lowest_grade = students_data[1][1]

print(second_lowest_grade)

for name, score in students_data:
    if score == second_lowest_grade:
        print(name)