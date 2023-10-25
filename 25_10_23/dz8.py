# def to_nine(number):
#     a = ''
#     while number > 0:
#         a += str(number % 9)
#         number //= 9
#     return a[::-1]
#
#
# counter = 0
# for i in range(10**6, 10**7):
#     nine_number = to_nine(i)
#     if nine_number.count("6") == 1 and len([l for l in nine_number if int(l) % 2 == 1]) == 2:
#         print(to_nine(i))
#         counter += 1
#
# print()
# print(counter)


from itertools import product

count = 0
for p in product("012345678", repeat=7):
    if p.count("6") == 1 and p[0] != "0" and (p.count("1") + p.count("3") + p.count("5") + p.count("7")) == 2:
        count += 1
print(count)
