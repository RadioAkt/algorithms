from math import *

# #№1
# a = []
# for i in range(1, 201):
#     i **= 2
#     a.append(i)
# print(sum(a))

# #№2
# n = int(input())
# c_1 = []
# c_2 = []
# c_3 = []
# c_0 = []
# i = 1
# while i < n:
#     a = int(input('Введите число: \n 1 – если вы изучали английский язык \n 2 – если немецкий, \n 3 – если французский, \n 0 – если не изучал никакой. \n '))
#     if a == 1:
#         c_1.append(i)
#         i += 1
#     if a == 2:
#         c_2.append(i)
#         i += 1
#     if a == 3:
#         c_3.append(i)
#         i += 1
#     if a == 0:
#         c_0.append(i)
#         i += 1
#     else:
#         pass
    
# print(f'Цифру "1" выбрали участники под номерами: {c_1}, \n Цифру "2" выбрали участники под номерами: {c_2}, \n Цифру "3" выбрали участники под номерами: {c_3}, \n Цифру "0" выбрали участники под номерами: {c_0}')

# #№3

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# i = 0
# for n1 in num:
#     for n2 in num:
#         for n3 in num:
#             for n4 in num:
#                 for n5 in num:
#                     for n6 in num:
#                         if n1 + n2 + n3 == n4 + n5 + n6:
#                             i += 1
# print(i)

#№4

# a = 1.0
# result = 0.0
# c = []
# for i in range(1, 104, 2):
#     c.append(i)
#     for j in c:    
#         result = 1.0 / (j + result)
# print(result)

#№5

# n = int(input())
# res = 0
# for i in range(1, n + 1):
#     num = 1
#     for j in range(i, 2 * i + 1):
#         num *= j
#     res += num
# print(res)

#№6

# def sigma():
#     res = 0
#     for i in range(3, 104):
#         res += 1/ (2 * i) ** 2
#     print(res)

# sigma()

#№7

# n = int(input())
# s = set()
# for i in range(1, int(n**0.5) + 1):
#     if n % i == 0:
#         s.add(i)
# if sum(s) == n:
#     print(f"число {n} - совершенное")
# else:
#     print(f"число {n} - не совершенное")

#№8

# def sigma():
#     res = 0
#     for i in range(1, 41):
#         if i % 2 != 0:
#             a = i
#             b = i**2
#             res += (a - b)**2
#         else:
#             a = i - 1
#             b = i**3
#             res += (a - b)**2
#     print(res)

# sigma()

#№9
# def f(x):
#     res = 1
#     for i in range(1,7):
#         res *= (x - 2**i)/(x - i + (i + 1))
#     print(res)


# x = int(input())
# f(x)

#№10

# def bat(R):
#     k = 0
#     for x in range(int(-R), int(R) + 1):
#         y = int(sqrt(R**2 - x**2))
#         k += (2 * y + 1) 
#     print(k)

# R = float(input())
# bat(R)

#№11

# def f(a,n):
#     res = 0
#     for i in range(1, 2*n, 2):
#         res += 1/(a**i)
#     print(res)

# a, n =map(int, input().split())
# f(a,n)

#№12

# def f(a,n):
#     res = 0
#     for i in range(1, n):
#         res += a * (a + i)
#     print(res)

# a, n =map(int, input().split())
# f(a,n)

#№13

# def f():
#     res = 1
#     a = 0.1
#     while a <= 10:
#         res *= (1 + sin(a))
#         a += 0.1
#     print(res)
# f()

#№14

# def deli(x):
#     a = set()
#     for i in range(1, x + 1):
#         if x % i == 0:
#             a.add(i)
#     print(a)
#     if len(a) > 2:
#         print(f'У числа {x} - нет толлько простых делитлей')
#     else:
#         print(f'У числа {x} - есть только простые делитлеи')

# x = int(input())
# deli(x)

#№15

# x = int(input())
# def num_count(x):
#     if n == 0:
#         print('1')  
#     k = 0
#     while n > 0:
#         n //= 10  
#         k += 1  
#     print(k)
# num_count(x)

#№16
# def f(x):
#     a = []
#     for i in range(1, n + 1):
#         if x % i == 0:
#             a.append(i)
#     a.reverse()
#     print(a)

# n = int(input())
# f(n)

#№17


# def Fib(x):
#     Fib_nums = []
#     a, b = 1, 1
#     while a < N:
#         Fib_nums.append(a)
#         a, b = b, a + b  
#     print(Fib_nums)
# 
# N = int(input())
# Fib(N)

#№18

# def R(N):
#     v = []
#     for i in range(1,N+1):
#         v.append(int(input('Введите рост студента: ')))
#     print(f'Ср. рост студентов: {sum(v)/len(v)} \n Мин. рост студентов: {min(v)} \n Макс. рост студентов: {max(v)}')
# 
# N = int(input())
# R(N)

#№19

# def num(n):
#     print(str(n)[-2])

# n = int(input())
# num(n)

#№20

# u, v, n =map(int, input().split())
# def sigma(u, v, n):
#     a = u
#     b = v
#     z = 1
#     j = 0
#     for k in range(2, n):
#         p = a
#         a += 2 * b + a
#         b += 2 * p ** 2 + b
#         z *= (k + 1)
#         j += (a * b) / z
#     print(j)
# sigma(u, v, n)


#Задание 1

#№9

# def f(x):
#     sim = ''
#     if age % 10 == 1 and age % 100 != 11:
#         sim = 'год'
#         print(age, sim)
#     elif age % 10 in [2,3,4] and not (age %100 in [12,13,14]):
#         sim = 'года'
#         print(age, sim)
#     else:
#         sim = 'лет'
#         print(age, sim)
    
# age = int(input())
# f(age)

#№10

# def number_to_words(n):
#     f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
#          6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
#     o = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
#          50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
#          80: 'восемьдесят', 90: 'девяносто'}
#     s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
#          14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
#          17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
#     n1 = n % 10
#     n2 = n - n1
#     if n < 10:
#         return f.get(n)
#     elif 10 < n < 20:
#         return s.get(n)
#     elif n >= 10 and n2 == 0:
#         return o.get(n)
#     else:
#         return 'Введено недостимое число!'

# a = int(input())

# print(number_to_words(a))