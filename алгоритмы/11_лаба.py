from random import *
#Задание 1

#3

# a = []
# n = int(input())
# for i in range(1, n + 1):
#     a.append(2**i)

# print(a)

#4

# a = [randint(200, 1000) for i in range(10)]
# print(a)
# even = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         even += 1
# print(even)

#5

# a = [randint(0, 80) for i in range(10)]
# print(a)
# b = []

# for i in range(len(a)):
#     if a[i] >= 50:
#         b.append(a[i])
# print(b)

# sr = sum(b)/len(b)
# print(sr)

#Задаине 2
#1
# a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'i']
# c = []
# for i in range(0, len(a)):
#     if i % 2 == 0:
#         c.append(a[i + 1])
#     else:
#         c.append(b[i - 1])
# print(c)

#2

# a = [randint(1, 50) for i in range(15)]
# print(a)
# b = []

# for i in range(len(a)):
#     if int(a[i] / 100 * 10) != 0:
#         b.append(int(a[i] / 100 * 10))
#         b.append(int(a[i] % 10))
#     else:
#         b.append(int(a[i] % 10))

# print(b)
# print(sum(b))

#3

# a = [[1, 2, 3], 
#      [4, 5, 6], 
#      [7, 8, 9]]

# b = []
# c = []

# for i in range(len(a)):
#     for j in range(len(i)):
#         if j < i:
#             b.append(a[i][j])
#         else:
#             b.append(a[j][i])

# for i in range(len(a)):
#     for j in range(len(i)):
#         if j < i:
#             c.append(a[i][j])
#         else:
#             c.append(-a[i][j])

# print(b)

# print(c)

#4

# m = int(input())
# n = int(input())

# ma = []
# for i in range(m):
#     row = list(map(float, input(f"Строка {i + 1}: ").split()))
#     ma.append(row)

# max_elem = abs(ma[0][0])
# for i in range(m):
#     for j in range(n):
#         if abs(ma[i][j]) > max_elem:
#             max_elem = abs(ma[i][j])


# new_ma = []
# for i in range(m):
#     new_row = []
#     for j in range(n):
#         new_row.append(ma[i][j] / max_elem)
#     new_ma.append(new_row)

# for row in new_ma:
#     print(" ".join(map(str, row)))


#5
# m = [[1, -2, 3],
#      [4, 0, -6],
#      [7, 8, 9]]

# a = []
# b = []
# c = []

# for i in range(len(m)):
#     for j in range(0, 3):
#         if i == 0:
#             a.append(m[i][j])
#         if i == 1:
#             b.append(m[i][j])
#         if i == 2:
#             c.append(m[i][j])
# print(a, b, c)
# print(sum(max(a, b, c)))

#6

# a = [[1, 2, 3], 
#      [4, 5, 6], 
#      [7, 8, 9]]
# mx = -9876543
# max = []
# mn = 98765432
# min = []
# for i in range(len(a)):
#     for j in range(0, i + 1):
#         if a[i][j] > mx:
#             mx = a[i][j]
#             max.append(a[i])
#         if a[i][j] < mn:
#             mn = a[i][j]
#             min.append(a[i])

# print(mx, mn)
# print(max[-1], min[-1])

# mx_el = max[-1]
# id_1 = a.index(mx_el)

# mn_el = min[-1]
# id_2 = a.index(mn_el)

# a[id_1], a[id_2] = a[id_2], a[id_1]

# print(a)

#7

# m = [
#     [3, 1, 4],
#     [1, 5, 9],
#     [2, 6, 5]
# ]


# mx_e = []
# id = []

# for i in range(len(m)):
#     mx_val = m[i][0]
#     mx_id = 0
#     for j in range(1, len(m[i])):
#         if m[i][j] > mx_val:
#             mx_val = m[i][j]
#             mx_id = j
#     mx_e.append(mx_val)
#     id.append((i, mx_id))


# min_of_max = mx_e[0]
# min_index = 0

# for i in range(1, len(mx_e)):
#     if mx_e[i] < min_of_max:
#         min_of_max = mx_e[i]
#         min_index = i

# final_indices = id[min_index]

# print(min_of_max)
# print(final_indices)

#8

# n = 12


# m = [[float(input(f"Введите элемент [{i}][{j}]: ")) for j in range(n)] for i in range(n)]


# for i in range(n):
#     for j in range(n):
#         if i == j:
#             m[i][j] = 0  
#         elif j > i:
#             m[i][j] = 1  

# for row in m:
#     print(row)

#9

# n = 11

# m = []
# print()
# for i in range(n):
#     row = list(map(float, input(f"Строка {i + 1}: ").split()))
#     m.append(row)

# result = [[0] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if m[i][j] > m[i][i]:  
#             result[i][j] = 1
#         else:
#             result[i][j] = 0

# for row in result:
#     print(row)

#10

# n = int(input())

# m = []
# for i in range(n):
#     row = list(map(float, input(f"Строка {i + 1}: ").split()))
#     m.append(row)

# is_sym = True

# for i in range(n):
#     for j in range(n):
#         if m[i][j] != m[j][i]:  
#             is_sym = False
#             break
#     if not is_sym:
#         break

# if is_sym:
#     print()
# else:
#     print()