#Задание 1
# kor = (1, 2, 3, 4, 5)
# sum = 0

# for i in kor:
#     print(i, end=' ')

# for i in range(5):
#     sum += kor[i]

# print("\n", sum)


# kor = (17, 109, 7, 15, 22)
# k = 0
# a = int(input('Введите число, больше которого необходимо отобрать значения: '))
# for i in kor:
#     print(i, end=' ')
# for i in range(5):
#     if kor[i] > a:
#         k += 1
    
# print("\n", k)

#Задание 2

# kor_1 = (1, 2, 3, 4)
# kor_2 = (5, 6)
# kor_2 += kor_1
# print(kor_2)

#Задание 1.2

# kor = (-11, - 12, 35, -8, -25, 39, 0, -12)

# k = 0

# proizv = 1

# for i in range(8):
#     if i % 2 == 1:
#         if kor[i] < 0:
#             proizv *= kor[i]
#             k += 1

# print(proizv, k)

#Задание 2.2

# kor = (-11, -12, 35, -8, -25, 39, 0, -12)
# k = 0
# sum = 0
# for i in range(8):
#     if kor[i] > 0:
#         sum = sum + kor[i] * kor[i]
#         k += 1
#         sr = sum/k

# print(sr, k)

#Задание 3.2

# kor = (24, 35, 29, 44, 8, 22, 4)

# inv = 0
# for i in range(6):
#     if kor[i] > kor[i + 1]:
#         inv += 1

# print(inv)

#Задание 4.2

# kor = (5.8, -1.7, 0, -7.5, 1.2, 0.8, 0.2)

# spi = []

# n = 0

# proizv = 1

# for i in range(7):
#     if kor[i] > 0:
#         spi.append(kor[i])
#         n += 1

# for i in range(n):
#     proizv = proizv * spi[i]

# print(spi, n, proizv)


#ДЗ

#1

# kor = (-4, -2, 3, 1, 2, -1)

# minkor = []

# for i in range(6):
#     if kor[i] < 0:
#         minkor.append(kor[i])

# print(minkor[-1])

#2

# def f(diameters, weights, max_weight_difference):
#     matching_pairs = []
    
#     for i in range(len(diameters)):
#         for j in range(i + 1, len(diameters)):
#             if abs(diameters[i] - diameters[j]) <= 1 and abs(weights[i] - weights[j]) <= max_weight_difference:
#                 matching_pairs.append(((diameters[i], weights[i]), (diameters[j], weights[j])))
    
#     return matching_pairs

# diameters = (15, 16, 17, 15, 18, 16)
# weights = (7.5, 8.0, 7.8, 7.6, 8.2, 7.9) 
# max_weight_difference = 0.5 


# matching_tires = f(diameters, weights, max_weight_difference)

# if matching_tires:
#     print("Подходящие пары шин: ")
#     for pair in matching_tires:
#         print(f"Шина 1: Диаметр = {pair[0][0]} см, Вес = {pair[0][1]} кг; "
#               f"Шина 2: Диаметр = {pair[1][0]} см, Вес = {pair[1][1]} кг")
# else:
#     print("Нет подходящих пар шин.")

#3

# a = (-1, -2, -3, -4, -5, 1, 2, 3, 4, 5)

# b = []

# for i in range(10):
#     if a[i] > 0:
#         b.append(a[i])

# b.sort
# print(b[0], b[-1])


#4

# kor = (17, 109, 7, 15, 22)
# k = 0
# sum = 0
# a = int(input('Введите число, больше которого необходимо отобрать значения: '))

# for i in range(5):
#     if abs(kor[i]) > a:
#         k += 1
#         sum += kor[i]

# sr = sum/k
    
# print(sr)

#5

# a = (160, 166, 170, 180)
# b = (163, 170, 180, 197)

# for i in a:
#     print(i, end=' ')

# for i in b:
#     print(i, end=' ')

# for i in range(4):
#     for j in range(i):
#         if a[i] == b[j]:
#             print("\n", a[i], b[j])

#6

# a = (1, 2, 2, 4, 5, 6, 7, 8, 9, 7)

# for i in range(10):
#     for j in range(i):
#         if a[i] == a[j]:
#             print("True")

#7

# a = (-1, -2, -3, -4, -5, 1, 2, 3, 4, 5)

# pr = 1

# for i in range(10):
#     if a[i] < 0 and i % 2 == 1:
#         pr *= a[i]

# print(pr)

#8

# def even_odd(x):
#     lst = list(x)

#     for i in range(0, len(lst) - 1, 2):

#         lst[i], lst[i + 1] = lst[i + 1], lst[i]
    
#     return tuple(lst)

# a = (1, 2, 3, 4, 5, 6)
# res = even_odd(a)
# print(res)