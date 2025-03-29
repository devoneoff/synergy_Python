# Задание 1
# С помощью цикла создайте матрицу вида 10x10.
# И ещё одну - такой же размерности. Числа в матрице выше привидены в качестве примера (одна из генераций)
# Итого у вас должно получиться сперва две матрица одинаковой размерности
# И теперь вам нужно сложить эти две матрицы в третью. Формулу сложения матриц, вы можете найти в интернете, либо посетив этот ресурс
# Итак. Вы должны создать две матрицы
# Чтобы заполнить матрицы различными значениями - воспользуйтесь модулем random
# И теперь нужно придумать, как их сложить, чтобы получить matrix_3
import random

def printList(t):
    print('[')
    for i in t:
        print(i)
    print(']')

matrix_1 = []
matrix_2 = []
matrix_3 = []

how = input("Матрицы квадратные (n x n)? Введите yes/no: ")
if how == "yes":
    x = int(input('Введите размерность матриц: '))
    for i in range(x):
        stroke = []
        for j in range(x):
            randomJ = random.randint(0, 100)
            stroke.append(randomJ)
        matrix_1.append(stroke)

    for i in range(x):
        stroke = []
        for j in range(x):
            randomJ = random.randint(0, 100)
            stroke.append(randomJ)
        matrix_2.append(stroke)

    for i in range(x):
        stroke = []
        for j in range(x):
            newValue = matrix_1[i][j] + matrix_2[i][j]
            stroke.append(newValue)
        matrix_3.append(stroke)
else:
    x = int(input('Введите количество строк: '))
    y = int(input('Введите количество столбцов в строке: '))
    
    for i in range(x):
        stroke = []
        for j in range(y):
            randomJ = random.randint(0, 100)
            stroke.append(randomJ)
        matrix_1.append(stroke)

    for i in range(x):
        stroke = []
        for j in range(y):
            randomJ = random.randint(0, 100)
            stroke.append(randomJ)
        matrix_2.append(stroke)

    for i in range(x):
        stroke = []
        for j in range(y):
            newValue = matrix_1[i][j] + matrix_2[i][j]
            stroke.append(newValue)
        matrix_3.append(stroke)

print("Первая матрица: ")
printList(matrix_1)
print("Вторая матрица: ")
printList(matrix_2)
print("Третья сложенная матрица: ")
printList(matrix_3)
