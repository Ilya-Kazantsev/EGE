import itertools
cnt = 0
arr = itertools.product('012345', repeat=3)
for i in arr:

    if list(i) == sorted(i, reverse=True) and i[0] != '0':
        cnt += 1
print(cnt)
