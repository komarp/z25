# Написать функцию которая на вход принимает списко чисел
# на выходе отдает число, которое встретилось нечетное количество раз
# такое число одно
from functools import reduce


def get_number(_list):
    return reduce(lambda x, y: x ^ y, _list)


if __name__ == '__main__':
    print(get_number([1, 1, 2, 2, 2, 3, 3]))
