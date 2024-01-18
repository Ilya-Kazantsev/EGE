import itertools
def func(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '30', 1)
        s = s.replace('02', '101', 1)
        s = s.replace('03', '202', 1)
    return s

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            st= '0'+'1'*i+'2'*j+'3'*k
            s = func(st)
            if (s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60):
                print('aaaa')
                print(st.count('1'))
                exit(0)
            print(st.count('1'))

