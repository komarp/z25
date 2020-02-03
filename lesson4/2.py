# Заполнить список вещественных чисел вводом с клавиатуры.
# Сколько элементов списка больше по модулю максимального числа.

# add code here
_max = 0
counter = 0
while True:
    a = input('Chislo >> ')
    if a == '':
        break
    else:
        try:
            if float(a) > _max:
                _max = float(a)
        except ValueError:
            print('Ошибка конвертирвания, введите число!')
        else:
            if abs(float(a)) > _max:
                counter += 1
print(counter)
