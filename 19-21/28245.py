def game(heap, moves, to):
    if heap >= 41:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [
        game(heap+1, moves+1, to),
        game(heap+10, moves+1, to)
    ]
    return any(h)


print(min(s for s in range(1, 41) if not game(s, 0, 1) and game(s, 0, 2)))

def game2(heap, moves, to):
    if heap >= 41:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [
        game2(heap+1, moves+1, to),
        game2(heap+10, moves+1, to)
    ]

    return any(h) if (moves+1) % 2 == to % 2 else all(h)

print(list(s for s in range(1, 41) if not game2(s, 0, 1) and game2(s, 0, 3)))
print(min(s for s in range(1, 41) if not game2(s, 0, 2) and game2(s, 0, 4)))

