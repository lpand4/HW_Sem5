# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 101 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

import random as r
num_of_candies = 101
print('Игра "Конфеты".\nЛежит 101 конфета.\nВы по очереди берете от 1 до 28 конфет за раз.')
print('Кто берет последнюю конфету, тот забирает все конфеты \n')
print('Проводим жеребьевку. У кого выпадет больше число из 100 - тот начнет первым')
print(f'')
choice_p = r.randint(0,100)
choice_c = r.randint(0,100)
if choice_p > choice_c:
    player = 1
    print(f'Ваше число {choice_p}. Число компьютера {choice_c}. \nВы победили, и начинаете первым\n')
else:
    player = 2
    print(f'Ваше число {choice_p}. Число компьютера {choice_c}. \nКомпьютер победил, и начинает первым\n')

def how_get():
    try:
        candy = int(input("Введите количество конфет, которое хотите взять(не более 28) - "))
    except:
        print("Введите число от 1 до 28")
        candy = -1
    while candy <= 0 or candy >= 29:
        try:
            candy = int(input("Введите количество конфет, которое хотите взять(не более 28) - "))
        except:
            print("Введите число от 1 до 28")
    return candy


while num_of_candies > 0:
    print(f'\nТекущее кол-во конфет = {num_of_candies}')
    if player == 1:
        print("Ход игрока")
        get1 = how_get()
        num_of_candies -= get1
        if num_of_candies <= 0:
            break
        player = 2
        continue
    else:
        print("Ход компьютера")
        get2 = r.randint(1,28)
        print(f'Компьютер взял {get2} конфет')
        num_of_candies -= get2
        if num_of_candies <= 0:
            break
        player = 1
if player == 1:
    print('Вы победили! Молодец!')
else:
    print('Победил компьютер!')