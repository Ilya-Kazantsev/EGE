for a in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not ((x < a)or (y > a) or (a < x-1) or (y < 2*x-3)):
                flag = False
    if flag:
        print(a)
        break