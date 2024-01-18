from itertools import permutations

table = '13 14 16 23 24 27 28 31 32 34 38 41 42 43 46 56 57 58 61 64 65 67 72 75 76 78 82 83 85 87'
graph = 'АБ АВ АГ АЖ БА БВ БД БИ ВБ ВА ВД ДБ ДВ ДИ ДЕ ЕД ЕГ ЕИ ЕЖ ГА ГЕ ГЖ ИБ ИЕ ИЖ ЖА ЖГ ЖЕ ЖИ ИД'

print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДЕИЖ'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(' '.join(p))