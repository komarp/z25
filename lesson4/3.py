# Заполнить список вещественных чисел вводом с клавиатуры.
# Найте элементы списка, которые меньше среднего арифметического.

# add code here
lst = []
while True:
    x = input('Chislo >> ')
    if x == '':
        break
    else:
        try:
            lst.append(float(x))
        except ValueError:
            print('Vvedite chislo !')
for num in lst:
    if num < (sum(lst) / len(lst)):
        print('Average > ', num)
