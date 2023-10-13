def f(n):
    a = n
    n_3 = ""
    while a > 0:
        n_3 = str(a % 3) + n_3
        a //= 3

    if n % 3 == 0:
        n_3 = n_3 + n_3[-3:]
    else:
        ost = (n % 3) * 3
        ost_s = ""
        while ost > 0:
            ost_s = str(ost % 3) + ost_s
            ost //= 3
        n_3 = n_3 + ost_s

    return int(n_3, 3)


for i in range(1, 15):
    if f(i) > 150:
        print(i, f(i))


# def f(n):
#     s = ''
#     while n > 0:
#         s = str(n % 3) + s
#         n //= 3
#     return s
#
#
# c = set()
# for n in range(1, 100):
#     s = f(n)
#     if n % 3 == 0:
#         s = s + s[-3:]
#     else:
#         s = s + f((n % 3) * 3)
#     r = int(s, 3)
#     if r > 150:
#         c.add(n)
#
# print(min(c))
