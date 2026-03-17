#Задание 1 

# #№4
# m = int(input('Введите номер месяца '))
# if m < 0 and m > 12:
#     print('Ошибка! Введён неверный номер месяца')
# elif m < 3 or m == 12:
#     print('Сейчас зима')
# elif m > 2 and m < 6:
#     print('Сейчас весна')
# elif m > 5 and m < 9: 
#     print('Сейчас лето')
# elif m > 8 and m < 12:
#     print('Сейчас осень')

#№8

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

#№9

# x = float(input("Введите координату по х:")) 
# y = float(input("Введите координату по у:")) 
# # пункт а
# if y < 1:
#     print('Вы попали в заштрихованную область!')
# else:
#     print('Вы не попали в заштрихованную область!')
# # пункт б 
# if y <= -x or x >= -y:
#     print('Вы попали в заштрихованную область!')
# else:
#     print('Вы не попали в заштрихованную область!')
# # пункт в
# if (x**2 + y**2 < 1) and -1<=x<=1 and -1<=y<=1 :
#     print('Вы попали в заштрихованную область!')
# else:
#     print('Вы не попали в заштрихованную область!')
# # пункт г
# if (x**2 + y**2 < 2) and (-1<=y<=1) and (0<=x<=2):
#     print('Вы попали в заштрихованную область!')
# else:
#     print('Вы не попали в заштрихованную область!')

# # #№10
# x = float(input("Введите координату по х:")) 
# y = float(input("Введите координату по у:")) 
# # пункт а
# # # 1 вариант
# if x <= 2 and y <= x and (x**2 + y ** 2 > 4):
#     print('Вы попали в заштрихованную область!')
# # # 2 вариант
# if x <= 2:
#     if y <= x:
#         if x**2 + y**2 >4:
#             print('Вы попали в заштрихованную область!')
# # пункт б
# # # # 1 вариант
# from math import *
# x = float(input("Введите координату по х:")) 
# y = float(input("Введите координату по у:"))
# if 0<=y<=0.5 and 0<=x<= pi and y<sin(x):
#     print('Вы попали в заштрихованную область!')
# # # # 2 вариант
# from math import *
# x = float(input("Введите координату по х:")) 
# y = sin(x)
# if 0<=y<=0.5:
#     if 0<=x<= pi:
#         if y<sin(x):
#             print('Вы попали в заштрихованную область!')

# # # пункт в
# # # # 1 вариант
# x = float(input("Введите координату по х:")) 
# y = float(input("Введите координату по у:")) 
# if (x > 0 and y <=2 and y < (2 - x**2)) or (x >= -2 and y < (2 - x**2) and y >=-2):
#     print('Вы попали в заштрихованную область!')
# # # # 2 вариант
# x = float(input("Введите координату по х:")) 
# y = float(input("Введите координату по у:")) 
# if x > 0:
#     if y <=2:
#         if y < (2 - x**2):
#             print('Вы попали в заштрихованную область!')
# elif x >= -2:
#     if y < (2 - x**2):
#         if y >=-2:
#             print('Вы попали в заштрихованную область!')

#Задание 2

#№1

# n = int(input())

# if n % 3 == 0:
#     print('Число кратно 3')
# else:
#     print('Число не кратно 3')

#№2/1

# x, y = map(int, input().split())

# z = (min(x, y) + 0.5) / (1 + (max(x, y) ** 2))

# print(z)

#№3/1

# x, y = map(int, input().split())

# if x < 0:
#     z = max(x, y)
#     print(z)
# else:
#     z = min(x, y)
#     print(z)

#№2/2

# x, y = map(int, input().split())

# if (x**2 + y**2 < 1) and -1<=x<=1 and -1<=y<=1:
#     print('Вы попали в заштрихованную область!')
# else:
#     print('Вы не попали в заштрихованную область!')

#№3/2

# x, y, z = map(int, input().split())

# L = 2 * max(x, z) - 3 * min(x, y, z)

# print(L)

#№4

# a, b, c = map(int, input().split())

# P = (max(a, b, c) - min(a, b, c)) / 2

# print(P)

#№5

# a, b = map(int, input().split())

# if a % 2 == 0 and b % 2 == 0:
#     print('Оба числа четные')
# if a % 2 != 0 and b % 2 != 0:
#     print('Оба числа нечетные')
# if a % 2 == 0 and b % 2 != 0:
#     print(f'Число "{a}" - четное, а число "{b}" - нечетное')
# if a % 2 != 0 and b % 2 == 0:
#     print(f'Число "{b}" - четное, а число "{a}" - нечетное')

#№6

# a, b, c = map(int, input().split())

# if a < b and b < c:
#     print('Неравенство выполняется')
# else:
#     print('Неравенство не выполняется')

#№7 

# a, b, c = map(int, input().split())

# if a >= b and b >= c:
#     a **= 2
#     b **= 2
#     c **= 2
#     print(a, b, c)
# else:
#     a = abs(a)
#     b = abs(b)
#     c = abs(c)
#     print(a, b, c)

#№8

# a, b = map(int, input().split())

# if a <= b:
#     a = 0
#     print(a, b)
# else:
#     print(a, b)

#№9

# x, y, z = map(int, input().split())

# if (x + y > z) and (y + z > x) and (x + z > y):
#     print('Треугольник существует')
# else:
#     print('Треугольник не существует')

#№10

# a = int(input())

# if a <= 2:
#     f = a ** 2 + 4 * a + 5
#     print(f)
# else:
#     f = 1 / (a ** 2 + 4 * a + 5)
#     print(f)

#№11

# a = int(input())

# if a > 1000:
#     b = a // 100 * 10
#     print(a - b)
# else:
#     print(a)

#№12

# a = int(input('введите день недели от 1 до 7 '))
# b = int(input())

# if a == 7:
#     c = b // 100 * 20
#     print(b - c)
# else:
#     print(b)

#№13

# a, b, c = map(int, input().split())

# if a > 0 and b > 0 and c > 0:
#     print((a + b + c) / 3)
# else:
#     print(a * b * c)

#№14

# a, b, c = map(int, input().split())

# d = []
# if a >0:
#     d.append(a**2)
# else:
#     d.append(a**4)
# if b >0:
#     d.append(b**2)
# else:
#     d.append(b**4)
# if c >0:
#     d.append(c**2)
# else:
#     d.append(c**4)
# print(*d)

#№15

# a, b, c = map(int, input().split())

# d = []

# if 3 < a and a <= 7:
#     d.append(a)
# if 3 < b and b <= 7:
#     d.append(b)
# if 3 < c and c <= 7:
#     d.append(c)
# print(d)

#№16

# x, y = map(int, input().split())

# if y < 0:
#     z = max(x ** 2, y ** 2)
#     print(z)
# else:
#     z = min(x, y)
#     print(z)

#№17

# x, y = map(float, input().split())

# if abs(x) <= 1 and abs(y) <= 1:
#     print('Точка принадлежит')
# else:
#     print('Точка не принадлежит')

#№18

# a, b, c, d = map(int, input().split())

# if a + b == c + d:
#     print('Билет счастливый')
# else:
#     print('Билет не счастливый')