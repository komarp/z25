"""
1. Создать функцию которая создает список
натуральных чисел от минимума до максимума с шагом
"""


def custom_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start
    _list = []
    while start < end:
        _list.append(start)
        start += step
    return _list


"""
2. Написать функцию такую что
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""


def accum(string):
    index = 1
    _list = []
    for sym in string:
        _list.append((sym * index).title())
        index += 1
    return '-'.join(_list)


# def accum(s):
#     return '-'.join([(sym * i).title() for i, sym in enumerate(s, 1)])


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


def points(_list):
    total = 0
    for item in _list:
        first, second = tuple(map(int, item.split(':')))
        # total = 3 if first > second else int(first == second)
        if first > second:
            total += 3
        elif first == second:
            total += 1

    return total


"""
4. Написать функцию, которая
определяет в списке наиболее встречаемое значение.
Вернуть значение и количество повторений.
"""


def max_number_count(_list):
    counter = {}
    for item in _list:
        counter[item] = counter.get(item, 0) + 1
    return max(counter.items(), key=lambda x: x[1])


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
