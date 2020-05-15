# Grading Students
# https://www.hackerrank.com/challenges/grading/problem

import os

def gradingStudents(grades):
    resultado = []
    for i in grades:
        if i < 38:
            resultado.append(i)
        elif i == 38 or i == 39:
            resultado.append(40)
        elif i % 5 == 0:
            resultado.append(i)
        else:
            a = i
            b = i
            while b % 5 != 0:
                b += 1
            if b - a < 3:
                resultado.append(b)
            else:
                resultado.append(a)
    return resultado   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
