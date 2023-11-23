import itertools
# itertools - библиотека для работы с комбинаторикой
# product() - функция, получающая все возможные перестановки элементов длины repeat из букв, которые в неё переданы
listString = itertools.product('АНДРЕЙ', repeat=7)
count = 0
for str in listString:
    # join() - функция соединяющая массив строк в одну строку при помощи разделителя, который указан до точки
    line = ''.join(str)
    # count() - строковая функция, которая определяет кол-во вхождений букв или слов в строку
    if line.count('Й') == 1 and line[0] != 'Й' and line.count('А') == 1:
        count += 1
print(count)