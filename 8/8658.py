import itertools
listString = itertools.product('УОА', repeat=6)
print([''.join(str) for str in listString].index('ОУУУОО')+1)