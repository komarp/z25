import time

"""
0. (*) Написать функцию, которая из списка чисел составляет
максимальное число
[98, 9, 34] -> 99834
"""


def max_number(_list):
    return ''.join(sorted(list(map(str, _list)), key=lambda x: x[0])[::-1])


"""
1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с
несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""


class MultiFileOpen:
    def __init__(self, file_name, meth):
        self.file_obj = open(file_name, meth)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(repr(exc_tb), repr(exc_val), repr(exc_type))
        self.file_obj.close()


"""
2.
Напишите менеджер контекста Timer, который позволяет получать текущее время
выполнения кода (отсчет начинается с конструкции with):
with Timer("Time: {}") as timer:
    do_some_logic()
    print(timer.now())  # Time: 3.4123 sec
    do_some_other_logic()
    print(timer.now())  # Time: 5.71 sec
"""


class Timer:
    def __init__(self, _str):
        self._str = _str
        self.start = time.time()

    def __enter__(self):
        return self

    def now(self):
        return self._str.format(self.start - time.time())

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(repr(exc_type), repr(exc_tb), repr(exc_val))


if __name__ == '__main__':
    assert max_number([234, 123, 98]) == 98234123
    assert max_number([1, 2, 3, 4]) == 4321
    assert max_number([]) is None
    assert max_number([98, 9, 34]) == 99834
    print('max_number - OK')
