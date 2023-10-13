def f(x, a_min, a_max):
    return ((a_min <= x <= a_max) <= (10 <= x <= 29)) or (13 <= x <= 18)


maxi = 0
for a_min in range(0, 1000):
    flag = True
    for a_max in range(a_min, 1000):
        for x in range(1000):
            if not f(x, a_min, a_max):
                flag = False
                break

        if not flag:
            break
        else:
            maxi = max(a_max - a_min, maxi)

print(maxi)


