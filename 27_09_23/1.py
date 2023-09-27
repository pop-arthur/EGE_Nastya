def f(a, x, y):
    return ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))


for a in range(1000):
    flag = True
    for x in range(100):
        for y in range(100):
            if not f(a, x, y):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
