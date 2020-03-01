"""
1.
Напишите итератор Fibonacci(n), который генерирует числа Фибоначчи до
n включительно.
"""


class Fib:
    def __init__(self, num):
        self.num = num
        self.cnt = 0

    def __next__(self):
        lst = [1, 1]
        while lst[-1] <= self.num:
            lst.append(lst[-1] + lst[-2])
        if lst[self.cnt] <= self.num:
            phase = self.cnt
            self.cnt += 1
            return lst[phase]
        raise StopIteration


"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""


class Even:
    def __init__(self, num):
        self.num = num
        self.start = 0

    def __next__(self):
        if self.start <= self.num:
            run = self.start
            self.start += 2
            return run
        raise StopIteration


"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


class Factorials:
    def __init__(self, num):
        self.num = num
        self.cnt = 0

    def __next__(self):
        lst = []
        val = 1
        for i in range(1, self.num + 1):
            val *= i
            lst.append(val)
        if self.cnt <= len(lst):
            phase = self.cnt
            self.cnt += 1
            try:
                return lst[phase]
            except IndexError:
                raise StopIteration


"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""
