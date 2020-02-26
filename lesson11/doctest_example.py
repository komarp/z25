def my_sum(a, b):
    """
    >>> my_sum(1, 2)
    3
    """
    return a + b


def foo(a):
    """
    >>> foo(1)
    1
    >>> foo(6)
    6
    >>> foo(5)
    Traceback (most recent call last):
    ...
    Exception: It's five
    """
    if a == 5 or a == 6:
        raise Exception("It's five")
    return a


if __name__ == '__main__':
    import doctest
    doctest.testmod()
