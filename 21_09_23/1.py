def f(a):
    a_str = str(a)
    b = int(a_str[0]) + int(a_str[1])
    c = int(a_str[1]) + int(a_str[2])
    if b > c:
        d = str(b) + str(c)
    else:
        d = str(c) + str(b)
    return int(d)


# func_result = f(348)
# print(func_result)
for i in range(100, 1000):
    func_result = f(i)
    if func_result == 1711:
        print(i)


a = bin(3)[2:]
print(a)
a = oct(9)[2:]
print(a)
a = int("15", 12)
print(a)

print("1010"[1::2])

