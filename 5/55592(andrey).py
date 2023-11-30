def f2(n):
    b = bin(n)[2:]
    even_count = len([i for i in str(n) if i in '2468'])
    odd_count = len([i for i in str(n) if i in '1357'])
    if even_count > odd_count:
        b += '1'
    elif even_count < odd_count:
        b += '0'
    else:
        if n % 2 == 0:
            b += '0'
        else:
            b += '1'
    return int(b, 2)


def f1(n):
    r1 = f2(n)
    r2 = f2(r1)
    r3 = f2(r2)
    return r3

count = 0
for i in range(1, 10000000):
    # print(f'{i} -> {f1(i)}')
    if 987654321 >= f1(i) >= 123455:
        count += 1
print(count)
