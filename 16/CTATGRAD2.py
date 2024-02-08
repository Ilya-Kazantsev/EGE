import sys
import itertools
sys.setrecursionlimit(100000000)
def f(n):
    if n == 0:
        return 0
    if n% 2 == 0:
        return f(n//10)+(n%10)
    else:
        return f(n//10)
cnt = 0
print(len(list(itertools.product('013579', repeat=9))))
for i in range(1, 100):
    if f(i) == 0:
        print(i, f(i))
        cnt += 1
print(cnt)