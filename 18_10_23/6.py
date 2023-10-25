import itertools


# a = ["Борщ", "Пицца", "Шаурма"]

# for elem in itertools.permutations(a, r=3):
#     print(elem)

# for elem in itertools.product(a, repeat=4):
#     print(elem)

letters = "ABCD"
count = 0
for elem in itertools.product(letters, repeat=5):
    # elem - список символов
    if elem.count("В") != 1:
        continue
    print(elem)
    count += 1

print(count)
print("УБИТО!")

a = [elem for elem in itertools.product(letters, repeat=5)]
b = sorted(elem for elem in itertools.product(letters, repeat=5))
print(a == b)