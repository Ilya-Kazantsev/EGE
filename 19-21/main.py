'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень или
увеличить количество камней в куче в два раза.
Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается в тот момент, когда количество камней в куче становится не менее 106. Победителем считается игрок,
сделавший последний ход, т.е. первым получивший кучу, в которой будет 106 или больше камней.

В начальный момент в куче было S камней; 1 ≤ S ≤ 105.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Описать стратегию игрока — значит, описать, какой ход он должен сделать в любой ситуации, которая ему может
встретиться при различной игре противника.

19
Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
Укажите минимальное значение S, когда такая ситуация возможна.

Ответ: 27

20
Найдите два таких значения S, при которых у Пети есть выигрышная стратегия,
причём одновременно выполняются два условия:
— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания без разделительных знаков.

Ответ: 2651

21
Найдите минимальное значение S, при котором одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом
при любой игре Пети;
— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

Ответ: 50
'''


def game(heap, moves, to):
    if heap >= 106:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap + 1, moves + 1, to),
         game(heap * 2, moves + 1, to)]
    # any(список_значений) - возвращает true, если хотя бы одно значение в списке истинно
    return any(h)


def game2(heap, moves, to):
    if heap >= 106:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game2(heap + 1, moves + 1, to),
         game2(heap * 2, moves + 1, to)]
    # any(список_значений) - возвращает true, если хотя бы одно значение в списке истинно
    # all(список_значений) - возвращает true, если все значения в списке истинны
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

# Петя: 1 3 5
# Ваня: 2 4 6
print(f'19: {min(s for s in range(1, 106) if not game(s, 0, 1) and game(s, 0, 2))}')
print(f'20: {[s for s in range(1, 106) if not game2(s, 0, 1) and game2(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 106) if not game2(s, 0, 2) and game2(s, 0, 4))}')

