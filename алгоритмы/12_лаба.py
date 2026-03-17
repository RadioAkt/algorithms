#задание 1
#1

# a = [1, 2, 3, 4, 5, -2]

# min = 971486854
# id = []
# for i in range(len(a)):
#     if a[i] < min:
#         min = a[i]
#         id.append(i)
# print(a[i], i)

# a = [1, 2, 3, 4, 5, -2]
# new_a = []

# for i in range(len(a)):
#     new_a.append(a[i])
#     new_a.sort()

# b = 0

# for i in range(len(a)):
#     if new_a[0] == a[i]:
#         b = i

# print(new_a[0], b)

#2
# a = [1, -2, 3, -4, 5, -3]

# even = []

# for i in range(len(a)):
#     if a[i] % 2 == 0 and a[i] > 0:
#         even.append(a[i])

# if len(even) == 0:
#     print('В списке нет подходящего числа')
# else:
#     even.sort()
#     print(even[-1])

#3
# a = [5, -4, 3, -2, 1, -1, 2, -3, 4, -5, 5]
# max_a = [1]

# for i in range(len(a)):
#     if a[i] > max_a[0]:
#         max_a.remove(max_a[0])
#         max_a.append(a[i])
#     elif a[i] == max_a[0]:
#         max_a.append(a[i])

# print(len(max_a))

#4
# a = [5, -4, 3, -2, 1, -1, 2, -3, 4, -5, - 1]
# a.sort()
# b = set()

# for i in range(len(a)):
#     b.add(a[i])

# sorted(b)
# c = list(b)
# c.sort()

# print(c[:2])

#5
# from random import *

# a = [randint(0, 4) for i in range(10)]
# x = int(input('Введите число от 0 до 4: '))
# print(a)

# for i in range(len(a)):
#     if a[i] == x:
#         print(i)