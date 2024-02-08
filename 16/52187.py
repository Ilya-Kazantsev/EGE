import sys
sys.setrecursionlimit(100000000)
def f(n):
    if n == 0:
        return 0
    return f(n//10)+(n%10)
cnt = 0
for i in range(765432015, 1542613238):
    if f(i) > f(i+1):
        cnt +=1
    print(f(i))


print(cnt)