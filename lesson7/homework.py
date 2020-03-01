"""1. Написать кэширующий декоратор,
который принимает время (в секундах, сколько необюходимо хранить результат)

@cache(60)  # значит что результат функции foo будет хранится 60 секунд
def foo():
    pass
"""
import re
import time


def cache(seconds):
    def inner(func):
        def decorator(*args, **kwargs):
            if not hasattr(cache, '_cache'):
                cache._cache = {}
            cache_key = (
                args,
                tuple(sorted(kwargs.items(), key=lambda item: item[0]))
            )
            _time, result = cache._cache.get(cache_key, (None, None))
            current_time = time.time()
            if not _time or current_time - _time > seconds:
                print('Miss cache')
                result = func(*args, **kwargs)
                cache._cache[cache_key] = (current_time, result)
            else:
                print('From cache')
            return result
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


def counter(string="Count - {}"):
    def inner(func):
        def decorator(*args, **kwargs):
            decorator.count += 1
            print(func.__name__, string.format(decorator.count))
            return func(*args, **kwargs)
        decorator.count = 0
        return decorator
    return inner


"""
3.
Написать функцию, которая извлекает даты из строки.'
Допускаем что во всех месяцах 31 день
get_datetimes('Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
10-02-2018 Lorem Ipsum has been the industry a s x')
>>> ['12-01-2018', '10-02-2018']
"""


def get_datetimes(string):
    pattern = re.compile(r'((?:(?:[0-2]\d)|(?:3[01]))-(?:(?:0\d)|(?:1[0-2]))-\d{4})')  # noqa
    return pattern.findall(string)


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


def get_words(string, sym=('consonants', 'vowels')):
    regexps = {
        ('consonants', 'vowels'): r'\b[a-z]+\b',
        ('consonants', ): r'\b[^euiao\s]\w+\b',
        ('vowels', ): r'\b[euiao]\w+\b'
    }
    pattern = re.compile(regexps[sym], re.IGNORECASE)
    return pattern.findall(string)


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


def get_ping_info(string):
    pattern = re.compile(r'icmp_seq=(\d+).+time=([\d\.]+)')
    return pattern.findall(string)


if __name__ == "__main__":
    @cache(10)
    def foo():
        time.sleep(2)
        return True

    # start = time.time()
    # print(foo())
    # print(foo())
    # print(foo())
    # time.sleep(10)
    # print(foo())
    # end = time.time()
    # print('Time', end - start)

    @counter()
    def test_count():
        pass

    @counter()
    def test_count1():
        pass

    test_count()
    test_count()
    test_count1()
    test_count()
    test_count1()
    test_count()

    test_count1()

    print('$'*100)
    s = """
    'Lorem Ipsum is simply 12-01-2018 dummy text of
    the printing 10-13-2018 and typesetting industry.
    10-02-2018 Lorem Ipsum has been the industry a s x'
    """
    print(get_datetimes(s))

    print('$'*100)
    print(get_words('Lorem Ipsum is simply', sym=('consonants', 'vowels')))
    print(get_words('Lorem Ipsum is simply', sym=('consonants',)))
    print(get_words('Lorem Ipsum is simply', sym=('vowels',)))

    s = """
    64 bytes from 216.58.215.110: icmp_seq=0 ttl=54 time=30.391 ms
    64 bytes from 216.58.215.110: icmp_seq=1 ttl=54 time=30.667 ms
    64 bytes from 216.58.215.110: icmp_seq=2 ttl=54 time=33.201 ms
    64 bytes from 216.58.215.110: icmp_seq=3 ttl=54 time=30.140 ms
    64 bytes from 216.58.215.110: icmp_seq=4 ttl=54 time=31.822 ms
    """
    print(get_ping_info(s))
