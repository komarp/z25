from functools import reduce


def persistence(number):
    return 1 + persistence(reduce(lambda x, y: x * y, map(int, str(number)))) \
        if number >= 10 else 0


print(persistence(999))
