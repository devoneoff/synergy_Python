# Задание 1
side_a = float(input('Введите длину стороны а: '))
side_b = float(input('Введите длину стороны b: '))
perimeter = 2 * (side_a + side_b)
square = side_a * side_b
print('Периметр прямоугольника:', perimeter, '\nПлощадь прямоугольника:', square)

# Задание 2
number = int(input('Введите целое пятизначное число: '))
num1 = number // 10000
num2 = (number // 1000) % 10
num3 = (number // 100) % 10
num4 = (number // 10) % 10
num5 = number % 10

result = ((num4 ** num5) * num3) / (num1 - num2)
print(result)
