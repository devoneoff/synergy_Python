# Задание 1
# На вход подается 1 строка без пробелов. По данной строке определите, является ли она палиндромом (то есть, можно ли прочесть ее наоборот, как, например, слово "шалаш"). Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном случае.
stroke = input('Введите строку: ')
stroke.lower()
stroke_reverse = stroke[::-1]
if stroke == stroke_reverse:
    print('yes')
else:
    print('no')

print('Начальная строка:', stroke)
print('Конечная строка:', stroke_reverse)

# Задание 2
# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.
stroke = 'Hello world  this    is  Python      programming'
minus = stroke.split() 
stroke = ' '.join(minus)
print(stroke)
