import itertools


def convert(s):
    while '12' in s:
        s = s.replace('12', '4', 1)
    return s


for i in range(1, 100):
    s = '1' * (10 - i) + '12' * i
    s = convert(s)
    if s.count('1') + s.count('2') * 2 + s.count('4') * 4 == 25:
        print(i)
        break
