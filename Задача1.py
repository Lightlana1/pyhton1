#Программа, к-я принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

a = int(input('Введите номер дня недели: '))
if a == 1:
    print('Первый день недели - понедельник')
elif a == 2:
    print('Второй день недели - вторник')
elif a == 3:
    print('Третий день недели - среда')
elif a == 4:
    print('Четвертый день недели - четверг')
elif a == 5:
    print('Пятый день недели - пятница')
elif a == 6:
    print('Ура! Выходной! Шестой день недели - суббота')
elif a == 7:
    print('Ура! Выходной! Седьмой день недели - воскресенье')
else:
    print('Вы ввели неверное число')