# Создайте программу для игры в ""Крестики-нолики"".
# def choice_pole(player):
def check_win(pole):
    win_condition = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in win_condition:
        if pole[item[0]] == pole[item[1]] == pole[item[2]]:
            return pole[item[0]]
    return False


def player_choice(pers):
    ok = False
    while not ok:
        try:
            choice = int(input("Введите позицию, куда хотите поставить свой знак - "))
        except:
            print('Необходимо ввести число!')
            continue
        if 1 <= choice <= 9:
            try:
                if str(pole[pole.index(choice)]) in 'XO':
                    print('Клетка уже занята!')
                else:
                    pole[pole.index(choice)] = pers
                    ok = True
            except:
                print('Клетка уже занята!')

        else:
            print('Вы ввели число не из диапазона 1 - 9')


print('Игра "Крестики-нолики".')
names = {}
names['X'] = input('Введите имя того, кто будет играть за "крестики" - ')
names['O'] = input('Введите имя того, кто будет играть за "нолики" - ')
print("Первым ход начинают 'крестики'\n")
player = 'X'
pole = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_player = None
count = 0
while count!=9:
    print(f'{pole[0], pole[1], pole[2]}\n{pole[3], pole[4], pole[5]}\n{pole[6], pole[7], pole[8]}\n')
    if player == 'X':
        player_choice('X')
        if check_win(pole) == False:
            player = 'O'
        else:
            win_player = 'X'
            break
    else:
        player_choice('O')
        if check_win(pole) == False:
            player = "X"
        else:
            win_player = 'O'
            break
    count+=1
print(f'{pole[0], pole[1], pole[2]}\n{pole[3], pole[4], pole[5]}\n{pole[6], pole[7], pole[8]}\n')
if win_player != None:
    print(f"Победил игрок {names[win_player]}!")
else:
    print("У Вас ничья!")
