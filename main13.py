# Задание 1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Kassa(object):
    money = 0

    def __init__(self, m):
        self.money = m

    def top_up(self):
        x = int(input("Введите сумму, на которую хотите пополнить кассу: "))
        self.money += x
    
    def count_1000(self):
        print(f'{self.money // 1000} целых тысяч осталось в кассе')
    
    def take_away(self):
        x = int(input('Введите сумму, которую хотите забрать из кассы: '))
        if self.money >= x:
            self.money -= x
            print(f'Вы забрали из кассы {x} руб. Осталось: {self.money}')
        else:
            print('Недостаточно денег в кассе')
            
k = Kassa(0)
command = ''
while command != 'выход':
    command = input('Что вы хотите сделать (пополнить, посмотреть, забрать, выход)? ')
    if command == 'пополнить':
        k.top_up()
    elif command == 'посмотреть':
        k.count_1000()
    elif command == 'забрать':
        k.take_away()
    elif command == 'выход':
        exit
    else:
        print('Извините, некорректная команда')



# Задание 2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход

# у этого класс есть методы:

# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

class Turtle(object):
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        self.print_status()

    def go_down(self):
        self.y -= self.s
        self.print_status()

    def go_left(self):
        self.x -= self.s
        self.print_status()

    def go_right(self):
        self.x += self.s
        self.print_status()

    def evolve(self):
        self.s += 1
        self.print_status()

    def degrade(self):
        if self.s <= 1:
            print("Ошибка: шаг не может быть меньше или равен 0.")
        else:
            self.s -= 1
            self.print_status()

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s
        print(f'Минимальное количество ходов: {max(moves_x, moves_y)}')

    def print_status(self):
        print(f'Текущие координаты: x = {self.x}, y = {self.y}, s = {self.s}')


t = Turtle()
cm = input('Введите "start" для начала: ')
if cm == 'start':
    command = ''
    t.print_status()
    while command != 'exit':
        command = input('Введите команду (go_up, go_down, go_left, go_right, evolve, degrade, count_moves, exit): ')
        if command == 'go_up':
            t.go_up()
        elif command == 'go_down':
            t.go_down()
        elif command == 'go_left':
            t.go_left()
        elif command == 'go_right':
            t.go_right()
        elif command == 'evolve':
            t.evolve()
        elif command == 'degrade':
            t.degrade()
        elif command == 'count_moves':
            x2 = int(input('Введите целевую координату x: '))
            y2 = int(input('Введите целевую координату y: '))
            t.count_moves(x2, y2)
        elif command == 'exit':
            print('Выход из программы.')
            break
        else:
            print('Извините, неверная команда.')
else:
    print('Извините, неверная команда. Напишите "start".')
