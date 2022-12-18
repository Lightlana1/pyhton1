import random

print('Условия игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \n'
      'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. '
      '\nВсе конфеты оппонента достаются сделавшему последний ход.')

def step(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = 'Компьютер'
print(f"Против вас играет {player2}")
value = int(input("Введите количество конфет на столе: "))
print('Жребий выберет, кто ходит первым')
count = random.randint(1,3)
if count == 1:
    print(f"Первый ход за игроком {player1}")
else:
    print(f"Первый ход за игроком {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if count % 2 != 0:
        k = step(player1)
        counter1 += k
        value -= k
        count = count + 1
        p_print(player1, k, counter1, value)
    else:
        k = random.randint(1,29)
        counter2 += k
        value -= k
        count = count + 1
        p_print(player2, k, counter2, value)

if count % 2 != 0:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")