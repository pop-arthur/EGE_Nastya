def f(x, y, a):
    func = ((2*x + 3*y) < a) or (x >= y) or (y > 24)
    # a <= b
    return func


# for a in range(1000):
#     flag = True
#     for x in range(1000):
#         for y in range(1000):
#             func = f(x, y, a)
#             if func == False:
#                 flag = False
#                 break
#         if flag == False:
#             break
#     if flag == True:
#         print(a)


for x in range(2):
    for y in range(2):
        print(x, y, '=', x <= y)
