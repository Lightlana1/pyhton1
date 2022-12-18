# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from typing import List, Any

with open('file.txt', 'w') as data:
    data.write('WWWBWWWBBBWWWBWWW')

with open('file.txt', 'r') as data:
    string = data.readline()

lst = list(string)
print(lst)
count = 0


def encode(s):
    encoding = ""

    i = 0
    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        encoding += str(count) + s[i]
        i = i + 1

    return encoding
lst2 = encode(lst)

print(encode(lst))

with open('file.txt', 'a') as file:
    file.write('\n' + lst2)
