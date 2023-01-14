# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# user_str = input("Введите текст - ")
user_str = 'aабвабвывыффывабвфыафыафывабв'
x = 'абв'
if x in user_str:
    result = user_str.replace(x, '')
print(result)
