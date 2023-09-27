# task 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in range(len(a)):
#     if a[i] < 5:
#         print(a[i])
# for elem in a:
#     if elem < 5:
#         print(elem)

# task 2
# a = [6, 20, 2, 18, 24, 1, 1, 24, 11, 22]
# print(sum(a))
# maxi = float("-inf")
# for i in range(len(a)):
#     for j in range(i):
#         maxi = max(a[i] + a[j], maxi)
# print(maxi)
# mini = float("inf")
# for i in range(len(a)):
#     for j in range(i):
#         mini = min(a[i] + a[j], mini)
# print(mini)

# task 3
# a = dict()
# for i in range(1, 11):
#     a[i] = i ** 3

#  task 5
# a = ['e', 't', 't', 'r', 'e', 'r', 'w', 'q', 'y', 'w', 'q', 'e', 'q', 'e', 'e']
# b = set(a)
# for elem in b:
#     print(a.count(elem))

# task 7
# def is_prime(a):
#     for i in range(2, a):
#         if a % i == 0:
#             return False
#     return True
#
#
# for i in range(5, 10):
#     print(i, is_prime(i))


# task 8
# def is_unique(a):
#     if len(a) == len(set(a)):
#         return True
#     return False
