def to_ternary(num):
    ans = ''
    while num > 0:
        ans = str(num % 3) + ans
        num //= 3
    return ans


for num in range(2, 1000):
    pr = to_ternary(num)
    if num % 3 == 0:
        pr += pr[-3:]
    else:
        pre = to_ternary(num % 3)
        pr += pre
    if int(pr, 3) > 150:
        print(num)
        break
