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


 ############## Class Queue ###################
class Queue:
    def __init__(self, size=None):
        self._size = size
        self._value = []


    def show_me(self):
        return 'Available size is', self._size, 'Value is', self._value


    def _perm_to_add(self):
        return self._size > len(self._value) or self._size is None



    def add(self, obj):
        if self._perm_to_add():
            self._value.append(obj)
        else:
            raise Exception('Too many obj')


    def _check_it_out(self):
            return  len(self._value) > 0


    def remove(self):
        if self._check_it_out():
            del self._value[0]
        else:
            raise Exception('Nothing to delete!')


 #################### Class Stack ################


class Stack(Queue):
    def __init__(self, size):
        super().__init__(size)


    def get(self):
        if self._check_it_out():
            a = self._value[-1]
            del self._value[-1]
            return a
        else:
            raise Exception('Nothing to get!')
