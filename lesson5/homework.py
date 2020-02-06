"""
1. Создать функцию которая создает список
натуральных чисел от минимума до максимума с шагом
"""


def custom_range(_min=0, _max=None, step=1):
    lst = []
    if _min and _max is None:
        _max = _min
        _min = 0
        while _min < _max:
            lst.append(_min)
            _min += step
    while _min < _max:
        lst.append(_min)
        _min += step
    return lst


"""
2. Написать функцию такую что
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""


def accum(str):
    res = [elem.capitalize() for elem in str.lower()]
    res2 = '-'.join([elem + elem.lower() * res.index(elem) for elem in res])
    return res2


"""
3. Our football team finished the championship.
The result of each match look like "x:y".
Results of all matches are recorded in the array.
For example: ["3:1", "2:2", "0:1", ...]
Write a function that takes such list and counts
the points of our team in the championship.
Rules for counting points for each match:
if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:
there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""


def points(lst):
    cnt = 0
    for elem in lst:
        cnt += 3 if int(elem[0]) > int(elem[2]) else 0
        if int(elem[0]) == int(elem[2]):
            cnt += 1
    return cnt


"""
4. Написать функцию, которая
определяет в списке наиболее встречаемое значение.
Вернуть значение и количество повторений.
"""
"""
return sorted(list({elem: lst.count(elem) for elem in lst}.items()), key = lambda x: x[1])[-1]
думал выпендреться в одну строку, но PEP:(
"""


def max_number_count(lst):
    _items = list({elem: lst.count(elem) for elem in lst}.items())
    return sorted(_items, key=lambda x: x[1])[-1]


if __name__ == '__main__':
    assert custom_range(1, 4) == [1, 2, 3]
    assert custom_range(1, 4, 2) == [1, 3]
    assert custom_range(1, 1, 2) == []
    assert custom_range(5) == [0, 1, 2, 3, 4]
    print('custom_range - OK')

    assert accum("abcd") == "A-Bb-Ccc-Dddd"
    assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    assert accum("cwAt") == "C-Ww-Aaa-Tttt"
    print('accum - OK')

    assert points(
        ['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2',
         '4:3']) == 30
    assert points(
        ['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4',
         '4:4']) == 10
    assert points(
        ['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4',
         '3:4']) == 0
    assert points(
        ['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4',
         '3:4']) == 15
    assert points(
        ['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4',
         '3:4']) == 12
    print('points - ok')

    assert max_number_count([1, 2, 2, 3, 3, 3]) == (3, 3)
    assert max_number_count([1, 2, 3, 1, 1]) == (1, 3)
    print('max_number_count - OK')
