# Вводятся два целых числа.
# Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть)
# и частное (в любом случае).

# add code here
try:
    a = int(input('Chislo1 >> '))
    b = int(input('Chislo2 >> '))
except ValueError:
    print('Введите число!')
else:
    try:
        if a % b is not False:
            print('NO', a // b, '\n', 'ostatok >> ', a % b)
        else:
            print('YES', a // b)
    except ZeroDivisionError:
        print('Деление на 0!')
