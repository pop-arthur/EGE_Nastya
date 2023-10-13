with open("2.txt") as file:
    num = file.readlines()

num = [[int(elem) for elem in row.split()] for row in num]

for row in num:
    if len(set(row)) != 4:
        continue

    pov1 = set(elem for elem in row if row.count(elem) == 1)
    pov2 = set(elem for elem in row if row.count(elem) == 2)
