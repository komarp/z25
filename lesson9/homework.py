"""
1*. Переписать код из homework6 используя ООП
2. Реализовать класс "очередь"
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
- в качестве инициализации принимает размер очереди, если параметр не указан,
то очередь - бесконечная
- выдать сообщение об ошибке, если в полную очередь добавить элемент нельзя,
или из пустой очереди достать элемент
3. Реализовать класс "стек"
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
- в качестве инициализации принимает размер стека, если параметр не указан,
то стек - бесконечный
- выдать сообщение об ошибке, если в полный стек добавить элемент нельзя,
или из пустого стека достать элемент
"""


class DataType:
    def __init__(self, size=None):
        self._size = size
        self._data = []

    def is_full(self):
        return self._size is not None and len(self._data) == self._size

    def is_empty(self):
        return not len(self._data)

    def pop(self):
        if self.is_empty():
            raise Exception(f"{self.__class__.__name__} is empty")
        return self._data.pop()

    def push(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self._push(item)

    def _push(self, item):
        self._data.insert(0, item)


class Queue(DataType):
    def get_queue(self):
        return '->'.join(map(str, self._data))


class Stack(DataType):
    def _push(self, item):
        self._data.append(item)

    def get_stack(self):
        return '\n^\n'.join(map(str, self._data[::-1]))


if __name__ == '__main__':
    q = Queue(5)
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q.get_queue())
    q.pop()
    print(q.get_queue())

    s = Stack(4)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    s.pop()
    s.pop()
    s.pop()
    s.pop()
