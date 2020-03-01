"""
1.
Напишите итератор Fibonacci(n), который генерирует числа Фибоначчи до
n включительно.
"""


"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""


"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


class BinomialCoefficients:
    def __init__(self, n):
        self.n = n
        self.numerator = 1
        self.count = 0
        self.denominator = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            result = self.numerator // self.denominator
            self.numerator *= (self.n - self.count)
            self.denominator *= (self.count + 1)
            self.count += 1
            return result
        raise StopIteration
