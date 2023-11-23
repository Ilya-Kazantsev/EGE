for n in range(100, 200):
    r = bin(n)[2:]
    r += bin(n % 3)[2:].zfill(2)
    n1 = int(r, 2)
    r += bin(n1 % 5)[2:].zfill(3)
    ans = int(r, 2)
    print(f'{n} -> {ans} -> {ans/n} -> {ans//n}')