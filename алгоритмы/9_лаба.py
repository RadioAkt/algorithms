import random

# #1
# s = random.sample(range(100), 7)
# print(s, end='')
# num = int(input('\n Введите число: '))
# s.append(num)
# print(s, end='')

#2
# s = random.sample(range(100), 7)
# print(s, end='')
# num = int(input('\n Введите число: '))
# poz = int(input('\n Введите позицию: '))
# s.insert(poz, num)
# print(s, end='')

#3
# s1 = random.sample(range(100), 7)
# print('\n First')
# print(s1, end='')
# s2 = random.sample(range(100), 7)
# print('\n Second')
# print(s2, end='')
# s1.extend(s2)
# print('\n', s1, end='')

# #4
# s = [8, 9, -7, 7, 0]
# for i in s:
#     print(i, end=' ')
# num = int(input())
# s.remove(num)
# print(s)

#5
# s = [8, 9, -7, 7, 0]
# for i in s:
#     print(i, end=' ')
# ind = int(input())
# sp = s.pop(ind)
# print(sp)
# print(s, end=' ')

#6

# s = random.sample(range(-100, 100), 25)
# for i in s:
#     print(i, end=' ')
# znach = int(input('\n'))
# k = s.count(znach)
# print(s, end=' ')
# print('\n', k)

#7

# s = random.sample(range(-100, 100), 25)
# print(s)
# s.sort()
# print(s)

#8

# s = random.sample(range(-10, 10), 7)
# print(s)
# s.reverse()
# print(s)

#9

# num = random.sample(range(100), 10)
# print(num, end=' ')

# nummin = 0
# nummax = 0

# min = 98765432
# max = -98765432

# for i in range(1, 10):
#     if num[i] < min:
#         min = num[i]
#     if num[i] > max:
#         max = num[i]
# print('\n', min)
# print('\n', max)

# min = num[nummin]
# num[nummin] = num[nummax]
# num[nummax] = min
# for i in range(0, 10):
#     print(num[i], end='\t')

#10

# from math import *
# n = int(input())
# x = random.sample(range(-5, 15), n)
# for i in x:
#     print(i, end=' ')
# c = int(input('\n введите значение перем: '))

# y = []
# for i in range(n):
#     if abs(x[i]) > c:
#         y.append(x[i])
# print(y)

#11

# n = int(input())
# s = []
# odd =[]
# even=[]

# for i in range(n):
#     sp = input()
#     s.append(sp)
# print(s)
# for i in range(n):
#     if i % 2 == 0:
#         odd.append(s[i])
#     else:
#         even.append(s[i])
# odd.sort()
# even.sort()
# print('\n', odd, '\n', even)


