from functools import lru_cache


def move(s):
    x = s[0]
    y = s[1]
    res = []
    if x > 1:
        res += [(x - 1, y), (round(x / 2 + 0.1), y)]
    if y > 1:
        res += (x, y - 1), (x, round(y / 2 + 0.1))
    return res


@lru_cache(None)
def game(s):
    if sum(s) <= 20:
        return 'win'
    elif any(game(mov) == "win" for mov in move(s)):
        return "p1"
    elif all(game(mov) == "p1" for mov in move(s)):
        return "v1"
    elif any(game(mov) == "v1" for mov in move(s)):
        return "p2"
    elif all(game(mov) in ("p1", "p2") for mov in move(s)):
        return "v12"


for i in range(11, 30):
    print(i, game((10, i)))
    # if game((10, i)) == "v1":
    #     print(i)
