"""
0. (*) Написать функцию, которая из списка чисел составляет
максимальное число
[98, 9, 34] -> 99834
"""
import time


class Cmp:
    def __init__(self, obj):
        self.obj = str(obj)

    def __lt__(self, other):
        return self.obj + other.obj < other.obj + self.obj


def max_number(_list):
    if _list:
        return int(''.join(map(str, sorted(_list, key=Cmp, reverse=True))))


"""
1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с
несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""


class MultiFileOpen:
    def __init__(self, *args):
        self._files = {}
        for file_name, mode in args:
            self._files[file_name] = open(file_name, mode)

    def __enter__(self):
        return self

    def __getitem__(self, item):
        return self._files[item]

    def __exit__(self, exc_type, exc_val, exc_tb):
        for file in self._files.values():
            file.close()


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
    def __init__(self, _str="Time: {}"):
        self._str = _str
        self._start = None

    def __enter__(self):
        self._start = time.time()
        return self

    def now(self):
        return self._str.format(time.time() - self._start)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':

    with MultiFileOpen(('file1.txt', 'w'), ('file2.txt', 'w')) as manager:
        manager['file1.txt'].write('hello')
        manager['file2.txt'].write('world')

    with Timer() as timer:
        print(timer.now())
        time.sleep(2)
        print(timer.now())

    assert max_number([234, 123, 98]) == 98234123
    assert max_number([1, 2, 3, 4]) == 4321
    assert max_number([]) is None
    assert max_number([98, 9, 34]) == 99834
    print('max_number - OK')
