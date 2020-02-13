import re
import time


"""1. Написать кэширующий декоратор,
который принимает время (в секундах, сколько необюходимо хранить результат)

@cache(60)  # значит что результат функции foo будет хранится 60 секунд
def foo():
    pass
"""


def cache(seconds):
    def inner(func):
        def decorator(*args, **kwargs):
            if not hasattr(cache, '_cache'):
                cache._cache = {}
            cache_key = (args)
            res = cache._cache.get(cache_key)
            if not res:
                res = func(*args, **kwargs)
                cache._cache[cache_key] = res, time.time()
            if time.time()- cache._cache[cache_key][1] >= seconds:
                delattr(cache._cache, cache_key)
            return res
        return decorator
    return inner

"""
2.
Написать декоратор, который считает сколько раз была вызвана функция и выводит
эту информации на экран.
В качестве аргумента(необязательного) декоратор может принимать
текст(форматированный), который
будет выводиться вместе с количеством вызовов. Если данный аргумент не передан,
то выводить текст по умолучанию(любой)
@counter():
def foo():
    return 1
foo(123)
>>> 'Count - 1'
>>> 1
foo("asd")
>>> 'Count - 2'
>>> 1
@counter("Text {}"):
def foo1():
    return 1
>>> 'Text 1'
>>> 1
"""


def counter(str):
    def inner(func):
        def decorator(*args, **kwargs):
            if not hasattr(counter, '_cnt'):
                counter._cnt = 1
            else:
                counter._cnt += 1
            print(f'{str} - {counter._cnt}')
            return func(*args, **kwargs)
        return decorator
    return inner


@counter('Text')
def foo():
    return 1


"""
3.
Написать функцию, которая извлекает даты из строки.'
Допускаем что во всех месяцах 31 день
get_datetimes('Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
10-02-2018 Lorem Ipsum has been the industry a s x')
>>> ['12-01-2018', '10-02-2018']
"""


text = '''Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
10-02-2018 Lorem Ipsum has been the industry a s x'''


def get_datetimes(txt):
    pattern = re.compile('\d{2}-\d{2}-\d{4}')
    return pattern.findall(txt)



"""
4.
Написать функцию, которая извлекает все слова,
начинающиеся на гласную(согласную). Какие слова извлекать - аргумент функции
get_words('Lorem Ipsum is simply', sym=('consonants', 'vowels'))
>>> ['Lorem', 'Ipsum', 'is', 'sumply']
get_words('Lorem Ipsum is simply', sym=('consonants',))
>>> ['Lorem', 'sumply']
get_words('Lorem Ipsum is simply', sym=('vowels',))
>>> ['Ipsum', 'is']
"""


text2 = 'Lorem Ipsum is simply'


def get_words(txt, code=None):
    if code == 'consonants':
        return re.compile(r'\b[^aeouiAEOUI\d -.\n]\w*').findall(txt)
    elif code == 'vowels':
        return re.compile(r'\b[aeouiAEOUI]\w+\b').findall(txt)
    else:
        return txt


"""
5. Написать функцию, которая группирует результат команды ping
((<icmp_seq>, <ttl>), ...)
s = "64 bytes from 216.58.215.110: icmp_seq=0 ttl=54 time=30.391 ms
64 bytes from 216.58.215.110: icmp_seq=1 ttl=54 time=30.667 ms
64 bytes from 216.58.215.110: icmp_seq=2 ttl=54 time=33.201 ms
64 bytes from 216.58.215.110: icmp_seq=3 ttl=54 time=30.140 ms
64 bytes from 216.58.215.110: icmp_seq=4 ttl=54 time=31.822 ms"
get_result(s)
>>> ((0, 30.391), (1, 30.667), (2, 33.201), (3, 30.140), (4, 31.822))
"""


s = """64 bytes from 216.58.215.110: icmp_seq=0 ttl=54 time=30.391 ms
64 bytes from 216.58.215.110: icmp_seq=1 ttl=54 time=30.667 ms
64 bytes from 216.58.215.110: icmp_seq=2 ttl=54 time=33.201 ms
64 bytes from 216.58.215.110: icmp_seq=3 ttl=54 time=30.140 ms
64 bytes from 216.58.215.110: icmp_seq=4 ttl=54 time=31.822 ms"""


def get_ping_info(text):
    lst = re.compile(r'\b\d{1}\b').findall(text)
    lst2 = re.compile(r'\d{2}.\d{3}[^.:]').findall(text)
    return tuple(zip(list(map(int,lst)), list(map(float,lst2))))


if __name__ == "__main__":
    pass
    assert foo() ==  1
    print('counter - OK')
    assert get_datetimes(text) == ['12-01-2018', '10-13-2018', '10-02-2018']
    print('get_datetimes - OK')
    assert get_words(text2, code='vowels') == ['Ipsum', 'is']
    assert get_words(text2, code='consonants') == ['Lorem', 'simply']
    assert get_words(text2) =='Lorem Ipsum is simply'
    print('get_words - OK')
    assert get_ping_info(s) == ((0, 30.391), (1, 30.667), (2, 33.201), (3, 30.14), (4, 31.822))
