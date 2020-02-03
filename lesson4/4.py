# Перевести число, введенное пользователем,
# в байты или килобайты в зависимости от его выбора.

# add code here
try:
    num = float(input('Chislo >> '))
except ValueError:
    print('Vvedite chislo !')
else:
    _type = input('Vvedite - "k" for kilobytes or "b" for bytes: ')
    if _type == 'b':
        num = num * 1024
        print('You num in kylobytes = ', num, 'bytes')
    elif _type == 'k':
        num = num / 1024
        print('You num in bytes = ', num, 'kilobytes')
    else:
        print('Vvedite "k" or "b" !')
