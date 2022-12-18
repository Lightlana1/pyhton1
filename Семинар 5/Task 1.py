# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
with open('file2.txt', 'w') as data:
    data.write('абв где абвуке орп эюя')

with open('file2.txt', 'r') as data:
    str = data.readline()

x = 'абв'
str2 = str.split()
for word in str.split():
    if x in word:
        str2.remove(word)
print(" ".join(str2))

with open('file2.txt', 'a') as file:
    file.write('\n' + " ".join(str2))