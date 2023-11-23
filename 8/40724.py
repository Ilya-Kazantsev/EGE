import itertools
listString = set(itertools.permutations('СВЕТЛАНА', 8))
count = 0
for str in listString:
    line = ''.join(str)
    if line.count('АА') == 0:
        count += 1
print(count)