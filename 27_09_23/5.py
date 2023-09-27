from functools import lru_cache


def moves(x):  # кол-во камней в куче
    return x + 1, x + 2, x + 3  # все возможные ходы


@lru_cache(None)
def game(x):
    if x > 20:
        return "Win"
    # если любой из ходов пети ведёт к победе, то Петя побеждает своим первым ходом
    elif any(game(move) == "Win" for move in moves(x)):
        return "P1"
    # если все возможные ходы ведут в позицию Пети1, то Ваня побеждет своим первым ходом
    elif all(game(move) == "P1" for move in moves(x)):
        return "V1"
    # если любой из ходов Пети ведёт в Ваню 1, то Петя побеждает вторым ходом
    elif any(game(move) == "V1" for move in moves(x)):
        return "P2"
    # если все возможные ходы ведут в позицию Пети2, то Ваня побеждает своим вторым ходом
    elif all(game(move) == "P2" for move in moves(x)):
        return "V2"
    # если любой из ходов ведёт в Ваню2, то Петя побеждает своим третьим ходом
    elif any(game(move) == "V2" for move in moves(x)):
        return "P3"
    elif all(game(move) == "P3" for move in moves(x)):
        return "V3"
    elif any(game(move) == "V3" for move in moves(x)):
        return "P4"
    elif all(game(move) == "P4" for move in moves(x)):
        return "V5"
    elif any(game(move) == "V5" for move in moves(x)):
        return "P5"
    elif any(game(move) == "P5" for move in moves(x)):
        return "V6"


for x in range(1, 25):
    if "V" in game(x):
        print(x)

# 19: 17