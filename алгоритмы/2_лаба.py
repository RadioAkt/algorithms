from math import *

#№1

# a = float(input('Введите длину ребра: '))

# Sgran = pow(a, 2)
# Sbokpov = 4 * pow(a, 2)
# V = pow(a, 3)

# print('Площадь грани куба: ', Sgran, 'Площадь боковой поверхности: ', Sbokpov, 'Объем куба V = a^3: ', V)

#№2

# a = int(input('Введите 2-х значное число: '))

# if a // 100 == 0:
#     b = a % 10
#     c = a // 10
#     print(b + c)
# else:
#     print('Число не 2-х значеное')

#№3

# a = int(input())
# b = float(input())

# c = []
# while a < 12:
#     while b < 3.2:
#         v = a * b
#         b += 0.2
#         a += 1
#         c.append(round(v, 1))
# print(c)
    

#№4

# a, b, c, d = map(int, input().split())
# print(min(a, b, c, d))

#№5

# r1, r2 = map(int, input(). split())

# a = [r1, r2]
# s = []
# for i in a:
#     S = pi * (i ** 2)
#     print(S)
#     s.append(round(S, 2))
#     print(s)
# k = s[1] - s[0]
# print(k)

#№6

# a, b, c, d = map(int, input().split())
# print(max(a, b, c, d))

#№7
# i = 2
# mi = 0
# while i < 21:
#     print("km = ", i)
#     mi = i / 1.609
#     i += 2
#     print('mile = ', mi)

#№8

# a, b, c = map(int, input(). split())
# print('a = ', a, "b = ", b, 'c = ', c)

# a = c
# c = b
# b = a

# print('a = ', a, "b = ", b, 'c = ', c)

#№9

# a, b, c = map(int, input().split())

# p = (a + b + c) / 2

# S = sqrt(p * (p - a) * (p - b) * (p - c))

# print(S)

#№10

# x, y = map(int, input().split())
# c = []
# if x > y:
#     c.append(x)
#     c.append(y)
#     c.sort
#     print('x = ', c[1], 'y = ', c[0])
# else:
#     print('x = ', x, 'y = ', y)

#№11

# a = int(input())
# s_a = a
# m = 12
# pr = 0.0076

# for i in range(m):
#     s_a += s_a * pr
# print(s_a)

#№12

# d1, d2 = map(int, input(). split())

# a = [d1, d2]
# s = []
# for i in a:
#     S = pi * (i ** 2)
#     print(S)
#     s.append(round(S, 2))
#     print(s)
# k = s[1] - s[0]
# print(k)

#№13 

# x1, y1, x2, y2, x3, y3 = map(int, input().split())

# s = 1/2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

# p = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# print(p, s)


#№14

# a, b, c = map(int, input().split())

# grad = radians(c)

# s = (a * b) * grad

# print(s)

#№15

# a = int(input())
# km = a
# nkm = 0.1
# t = 14
# a_t = 0
# for i in range(t):
#     a_t += nkm
#     nkm *= (1 + nkm)
# print(a_t)


#№16

# x, a, y = map(int, input().split())

# kg = a / x
# countkg = y * kg
# print('Стоймость 1 кг = ', kg)
# print('Стоимость ', y, 'кг цемента = ', countkg) 

# номер 1
Name = input('Введите имя, фамилию: ')
Town = input('Где Вы родились? ')
Mus = input('Какая музыка вам нравится? ')

print(f'Ваше имя и фамилия {Name}')
print(f'Вы родились в {Town}')
print(f'Ваша любимая музыка {Mus}')