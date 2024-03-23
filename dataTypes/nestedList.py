
#archivo = open("input.txt")
##print(archivo.read())
#input = archivo.read()

#primer numero es cantidad de estudiantes, seguido de nombre y calificacion para lograr segundo valor mas grande


if __name__ == '__main__':
    
    students_data = []
    students_scores = []
    for _ in range(int(input('Number of students:'))):
        name = input("Student's name:")
        score = float(input("Student's score:"))
        students_data.append([name, score])
        students_scores.append(score)

students_data.sort(key=lambda x : (x[1],x[0]))
second_lowest_grade = sorted(set(students_scores))[1]
print(students_data)
print(second_lowest_grade)
y= type(second_lowest_grade)
print(y)

for name, score in students_data:
    if score == second_lowest_grade:
        print(name)