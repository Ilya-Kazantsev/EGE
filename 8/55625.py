import itertools
cnt = 0
def c(i):
    ev = "ЯОА"
    for k in range(1, len(i)):
        if i[k] in ev and i[k-1] in ev:
            return False
    return True

arr = itertools.permutations('ЯРОСЛАВ', 5)

for i in arr:
    if i.count('Р')+i.count('С')+i.count('Л')+i.count('В') > i.count('Я')+i.count('О')+i.count('А') and c(i):
        cnt += 1
print(cnt)