# Задание 1
# Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
# Данная функция находит факториал полученного числа
# Например, факториал числа 3 это число 6.
# Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.
# В итоге, на вход программа получает например число 3, возвращает число 6 (факториал числа 3) и вам нужно сделать список из факториалов числа 6 в убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и так далее вплоть до 1
# То есть, результирующий список будет выглядеть в нашем примере так:
# [720, 120, 24, 6, 2, 1]

def factFact(summa_fact):
    list_factorials = []
    for j in range(summa_fact, 0, -1):
        fact = 1
        for k in range(1, j + 1):
            fact *= k
        list_factorials.append(fact)
    print(f'Все факториалы числа {summa_fact}:')
    print(list_factorials)

def factorial():
    number = int(input('Введите любое натуральное целое число: '))
    summa_fact = 1

    for i in range(1, number + 1):
        summa_fact *= i
    print(f'Факториал числа {number} равен {summa_fact}')

    factFact(summa_fact)

factorial()


# Задание 2
import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name
        }
    }
    print(f"Питомец {name} добавлен с ID {new_id}.")

def read(pet_id):
    pet_info = get_pet(pet_id)
    if pet_info:
        for name, details in pet_info.items():
            age_suffix = get_suffix(details["Возраст питомца"])
            print(f"Это {details['Вид питомца']} по кличке \"{name}\". Возраст питомца: {details['Возраст питомца']} {age_suffix}. Имя владельца: {details['Имя владельца']}.")
    else:
        print("Питомец с таким ID не найден.")

def update(pet_id):
    pet_info = get_pet(pet_id)
    if pet_info:
        name = list(pet_info.keys())[0]
        print(f"Обновление информации о питомце: {name}")
        pet_type = input("Введите новый вид питомца (оставьте пустым, если не хотите менять): ")
        age = input("Введите новый возраст питомца (оставьте пустым, если не хотите менять): ")
        owner_name = input("Введите новое имя владельца (оставьте пустым, если не хотите менять): ")
        
        if pet_type:
            pet_info[name]["Вид питомца"] = pet_type
        if age:
            pet_info[name]["Возраст питомца"] = int(age)
        if owner_name:
            pet_info[name]["Имя владельца"] = owner_name
        
        print(f"Информация о питомце {name} обновлена.")
    else:
        print("Питомец с таким ID не найден.")

def delete(pet_id):
    if pet_id in pets:
        del pets[pet_id]
        print(f"Питомец с ID {pet_id} удален.")
    else:
        print("Питомец с таким ID не найден.")

def get_pet(pet_id):
    return pets[pet_id] if pet_id in pets else False

def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

def pets_list():
    for pet_id, pet_info in pets.items():
        for name, details in pet_info.items():
            age_suffix = get_suffix(details["Возраст питомца"])
            print(f"ID: {pet_id}, Кличка: {name}, Вид: {details['Вид питомца']}, Возраст: {details['Возраст питомца']} {age_suffix}, Владелец: {details['Имя владельца']}")

# Основной цикл программы
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
    
    if command == "create":
        create()
    elif command == "read":
        pet_id = int(input("Введите ID питомца для чтения: "))
        read(pet_id)
    elif command == "update":
        pet_id = int(input("Введите ID питомца для обновления: "))
        update(pet_id)
    elif command == "delete":
        pet_id = int(input("Введите ID питомца для удаления: "))
        delete(pet_id)
    elif command == "list":
        pets_list()
    elif command != "stop":
        print("Неизвестная команда. Пожалуйста, попробуйте снова.")
