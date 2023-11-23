n = 1000
cnt = 0
def func(n):
    cntc = 0
    cntn = 0
    s = str(n)
    n = bin(n)[2:]
    for i in range(3):
        cntc = 0
        cntn = 0
        for i in range(len(s)):
            if (int(s[i]) % 2 == 0):
                cntc += 1
            else:
                cntn += 1
        if cntc > cntn:
            n += "1"
        elif cntc < cntn:
            n += "0"
        elif int(n, 2) % 2 == 0:
            n += "0"
        else:
            n += "1"
        n = int(n, 2)
        s = str(n)
        n = bin(n)[2:]
    return int(n, 2)

k = func(n)
while k <= 987654321:
    if k >= 123455:
        cnt += 1
        print(k)
    n += 1
    k = func(n)
print(cnt)

