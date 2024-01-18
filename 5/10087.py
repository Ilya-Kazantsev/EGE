def f(x):
    s = bin(x)[2:]
    if x % 3 == 0:
        s = s + s[-3:]

    else:
        ost = bin(x%3*3)[2:]
        s = s + ost
    return int(s, 2)


min = 1000000
for i in range(1, 1000):
    a = f(i)
    if a > 151 and a < min:
        min = a
print(min)
