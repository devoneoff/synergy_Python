# Задание 1
# Есть последовательность
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Напишите рекурсивную функцию, которая выведет все элементы от первого до последнего и в конце отобразит сообщение Конец списка, если выводить больше нечего. Циклы использовать запрещено
def print_list_recursive(my_list, index=0):
    if index < len(my_list):
        print(my_list[index])
        print_list_recursive(my_list, index + 1)
    else:
        print("Конец списка")
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list_recursive(my_list)
