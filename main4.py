# Задание 1
numbers = int(input('Введите количество чисел: '))
zeros = 0
for i in range(1, numbers + 1):
    number = int(input(f"Введите {i} число: "))
    if number == 0:
        zeros += 1
    else:
        continue
print("Количество чисел равных нулю:", zeros)

# Задание 2
number = int(input())
count = 0
divisors = []
for i in range(1, number):
    if number % i == 0:
        count += 1
        divisors.append(i)
    else:
        continue
print(f"Количество натуральных делителей числа {number}:", count, "\nДелители:", divisors)

# Задание 3
print("Число a <= b")
number_a = int(input("Число A: "))
number_b = int(input("Число B: "))
chet_numbers = []
for i in range(number_a, number_b):
    if i % 2 == 0:
        chet_numbers.append(i)
print(*chet_numbers)
