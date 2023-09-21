for num in range(2, 100):
    b = bin(num)[2:]
    b = b[:-1] + (b[1] * 2)
    r = int(b, 2)
    if r > 76:
        print(num)
        break
