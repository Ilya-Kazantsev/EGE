data = [list(map(int, line.split())) for line in open('64956.txt').readlines()[1:]]
data.sort()
# Время, в которое окно освобождается
posts = [[0, 0] for i in range(7)]
lefts = 0
for start_time, need_time, post in data:
    if start_time + 30 >= posts[post][0]:
        posts[post][0] = need_time + (start_time if posts[post][0] < start_time else posts[post][0])
        posts[post][1] += 1
    else:
        lefts += 1
print(lefts)
print(posts)