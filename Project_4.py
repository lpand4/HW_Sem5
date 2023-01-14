# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def archiv(msg,file = 'archive.txt'):
    count = 0
    result_msg = ''
    letter = None
    for i in range(len(msg)):
        if msg[i] == letter:
            continue
        else:
            letter = msg[i]
        for k in range(i, len(msg)):
            if msg[k] == letter:
                count += 1
            else:
                break
        result_msg += f'{count}{letter}'
        count=0
    with open(file,'w') as f:
        f.write(result_msg)

def vosstan(file):
    result_msg = ''
    with open(file,'r') as f:
        msg = f.read()
    for i in range(len(msg)):
        if msg[i].isdigit():
            for k in range(int(msg[i])):
                result_msg += msg[i+1]
    with open('vosstanovleniy.txt','w') as f:
        f.write(result_msg)
    return result_msg

msg1 = 'aaaabbcdddd'
archiv(msg1)
print(vosstan('archive.txt'))
