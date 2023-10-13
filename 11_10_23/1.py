with open("1.txt") as file:
    data = file.readlines()

data = [[float(elem.replace(",", ".")) for elem in row.split()] for row in data]
print(data)

data1 = list()
for row in data:
    data1.extend(row)
print(data1)

mini = min(data1)
print(mini)

avg = sum(data1) / len(data1)
print(avg)

print(mini - avg)