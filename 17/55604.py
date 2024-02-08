arr = open("55604.txt").readlines()
arr = [arr[i][:-1] for i in range(len(arr))]
maxx = -1
minn = 0
for i in range(len(arr)):
    if arr[i][-1] == arr[i][-2] and int(arr[i]) < minn:
        minn = int(arr[i])
cnt = 0
for i in range(len(arr)-1):
    if (arr[i][-1] == arr[i+1][-2] or arr[i][-2] == arr[i+1][-1]):
        if (abs(int((arr[i]))) % 7 == 0 and abs(int(arr[i+1]) % 7 != 0)) or (abs(int((arr[i]))) % 7 != 0 and abs(int(arr[i+1]) % 7 == 0)):
            if int(arr[i])**2+int(arr[i+1])**2 <= minn**2:
                cnt += 1
                if int(arr[i])**2+int(arr[i+1])**2 > maxx:
                    maxx = int(arr[i])**2+int(arr[i+1])**2
print(cnt, maxx)

