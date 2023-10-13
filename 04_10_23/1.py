from functools import lru_cache


def moves(s):
    # s = [x, y]
    # x - кол-во камней в 1 куче, y - во второй
    x = s[0]
    y = s[1]
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)


@lru_cache(None)
def game(s):
    # s = [x, y]
    if sum(s) >= 77:
        return "W"
    elif any(game(move) == "W" for move in moves(s)):
        return "P1"
    elif all(game(move) == "P1" for move in moves(s)):
        return "V1"
    elif any(game(move) == "V1" for move in moves(s)):
        return "P2"
    elif all(game(move) in {"P1", "P2"} for move in moves(s)):
        return "V12"


for i in range(1, 69 + 1):
    if game((7, i)) == "V12":
        print(i, game((7, i)))

# 19 - 18
