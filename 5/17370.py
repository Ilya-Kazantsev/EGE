ind = 0
arr = set()
for i in range(100, 3000):
    r = bin(i)[2:]
    ind = 0
    for j in range(len(r)):
        if r[j] == '1':
            ind = j+1
            while ind < len(r) and r[ind] != '1':
                ind += 1
            r = r[:j] + r[ind:]

            if r == "":
                arr.add(i)
            else:
                arr.add(i-int(r, 2))
            break
print(len(arr))

