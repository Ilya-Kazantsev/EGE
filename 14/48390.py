x = 0
y = 0
arr = []
for x in range(1, 8):
    for y in range(8):
        a = int(str(x) + "01" + str(y) + "4", 9)
        b = int(str(x) + str(y) + "544", 8)
        if (a+b)%89 == 0:
            arr.append(a+b)

print(min(arr)/89)
