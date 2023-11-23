max = 0
def to_ternary(num):
    ans = ''
    while num > 0:
        ans = str(num % 3) + ans
        num //= 3
    return ans
for i in range(1, 3000):
    r = to_ternary(i)
    if i % 3 == 0:
        r += r[-1]
        r += r[-3]
    else:
        r1 = to_ternary(i%3*5)
        r += r1
    r = int(r, 3)
    if r < 173:
        if r > max:
            max = r
        print(max)