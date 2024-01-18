
def func(arr):
    gl = 0
    fin = []
    for i in range(len(arr)):
        loc = 0
        for j in range(len(arr)):
            if arr[i] == arr[j] and arr[i] not in fin:
                loc += 1
        if loc == 2:
            gl += 1
            fin.append(arr[i])
    if gl != 2:
        return -1
    return float((fin[0]*2+fin[1]*2)/4)


cnt = 0

f = open("9_10091.txt")
for line in f:
    arr = list(map(int, line.split('\t')))
    div = func(arr)
    if div != -1 and div < sum(arr)/7:
        cnt += 1
print(cnt)


