def conv(s):
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    return s



minn = 101
minnn = 101
for i in range(100, 10000):
    s = '1'*i
    s = conv(s)
    if s.count('1') == 1:
        print(i)
        break

