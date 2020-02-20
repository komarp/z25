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
    def  __init__(self, width=None):
        self.__width  = width
        self.__value = []


    def show_me(self):
        print('Width is', self.__width, ';', 'Value is', str(self.__value))


    def __perm_to_add(self):
        if self.__width is None:
            return True
        elif self.__width > len(self.__value):
            return True
        else:
            return False


    def add(self, obj):
        if self.__perm_to_add():
            self.__value.append(obj)
        else:
            raise Exception('Too many obj')


    def __checknull(self):
            return True if len(self.__value) > 0 else False


    def remove(self):
        if self.__checknull():
            del self.__value[0]
        else:
            raise Exception('Nothing to delete!')


 #################### Class Stack################

class Stack:
    def __init__(self, size=None):
        self.__size = size
        self.__value = []

    def show_me(self):
        print('Available size is', self.__size, 'Value is', self.__value)

    def __perm_to_add(self):
        if self.__size is None:
            return True
        elif self.__size > len(self.__value):
            return True
        else:
            return False

    def add(self, obj):
        if self.__perm_to_add():
            self.__value.append(obj)
        else:
            raise Exception('Too many objects!')

    def __check_it_out(self):
        return False if len(self.__value) == 0 else True

    def get(self):
        if self.__check_it_out():
            a = self.__value[-1]
            del self.__value[-1]
            return a
        else:
            raise Exception('Nothing to get!')

