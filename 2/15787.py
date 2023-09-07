print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # Если функция в таблице равняется нулю, то необходимо поместить
                # всё выражение под знак отрицания not()
                if not(((x <= y) and (y <= w)) or (z == (x or y))):
                    print(x, y, z, w)
