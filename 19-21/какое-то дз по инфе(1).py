# def game(heap, moves, to):
#     if heap >=59:
#         return moves%2 == to%2
#     if moves == to:
#         return 0
#
#     h = [
#         game(heap+1, moves+1, to),
#         game(heap + 3, moves + 1, to),
#         game(heap * 4, moves + 1, to)
#     ]
#     return any(h) if (moves+1) % 2 == to % 2 else all(h)
#
#
# print(f'19: {min(s for s in range(1, 60) if not game(s, 0, 1) and game(s, 0, 2))}')
# print(f'20: {[s for s in range(1, 60) if not game(s, 0, 1) and game(s, 0, 3)]}')
# print(f'21: {min(s for s in range(1, 60) if game(s, 0, 2) or game(s, 0, 4) and not game(s, 0, 2))}')


def f(n):
    if n == 0:
        return 0
    return f(n//10)+f(n%10)
cnt = 0
for i in range(765432015, 1542613238):
    if f(i) > f(i+1):
        cnt +=1
print(cnt)