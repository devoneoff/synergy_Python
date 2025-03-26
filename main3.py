# Задание 1
# Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число". Если число не является четным - выведите сообщение "число не является четным"
number = int(input('Введите число: '))
if number == 0:
    print('Нулевое число')
elif number > 0:
    if number % 2 == 0:
        print('Положительное чётное число')
    else:
        print('Положительное нечётное число')
else:
    if number % 2 == 0:
        print('Отрицательное чётное число')
    else:
        print('Отрицательное нечётное число')

# Задание 2
# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False
word = input("Введите слово: ")
vowels = 'aeiou'
vowels_count = 0
consonants_count = 0

vowel_counts = {v: 0 for v in vowels}

for char in word:
    if char in vowels:
        vowels_count += 1
        vowel_counts[char] += 1
    else:
        consonants_count += 1
print('Количество гласных букв: ', vowels_count)
print('Количество согласных букв: ', consonants_count)

for v in vowels:
    if vowel_counts[v] == 0:
        print(f"Буквы '{v}' нет")
    else:
        print(f"Буква '{v}' встречается {vowel_counts[v]} раз(а)")

# Задание 3
# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
cash_Mike = float(input("Кэш Майка: "))
cash_Ivan = float(input("Кэш Ивана: "))
min_cash = float(input('Минимальная сумма инвестиций: '))

if (cash_Mike >= min_cash) and (cash_Ivan >= min_cash):
    print(2)
elif (cash_Mike >= min_cash) and (cash_Ivan <= min_cash):
    print('Mike')
elif (cash_Ivan >= min_cash) and (cash_Mike <= min_cash):
    print('Ivan')
elif (cash_Mike <= min_cash) and (cash_Ivan <= min_cash):
    if cash_Mike + cash_Ivan >= min_cash:
        print(1)
    else:
        print(0)
