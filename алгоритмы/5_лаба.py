# # import random
# 
# tests = {
#     'Задание 1': {
#         'Вопрос': ('В каком году появился язык Python?'),
#         'Варианты': [
#             "1. 1999 " "2. 1991 " "3. 1889 " "4. 2001"
#         ],
#         'Правильный ответ': ['2']
#     },
#     'Задание 2': {
#         'Вопрос': ('Как создать функцию в Python?'),
#         'Варианты': [
#             '1. func() ' '2. createfunction() ' '3. def f() ' '4. function()'
#         ],
#         'Правильный ответ': ['3']
#     },
#     'Задание 3': {
#         'Вопрос': ('Какой оператор используется для возведения числа в степень в Python?'),
#         'Варианты': [
#             '1. ^ ' '2. * ' '3. // ' '4. **'
#         ],
#         'Правильный ответ': ['4']
#     },
#     'Задание 4': {
#         'Вопрос': ('Какой метод используется для преобразования строки в целое число?'),
#         'Варианты': [
#             '1. int() ' '2. str() ' '3. float() ' '4. chr()'
#         ],
#         'Правильный ответ': ['1']
#     },
#     'Задание 5': {
#         'Вопрос': ('Какой цикл повторяется, пока условие истинно?'),
#         'Варианты': [
#             '1. for ' '2. while ' '3. repeat ' '4. foreach'
#         ],
#         'Правильный ответ': ['2']
#     }
# }

# def dysplay(test):
#     print(f"Вопрос: {test['Вопрос']}\n")

#     print(f"Варианты: {test['Варианты']}\n")

# def check_answer(user_answer, correct_answer):

#     user_answer_set = set(map(str, user_answer))

#     correct_answer_set = set(correct_answer)

#     return user_answer_set == correct_answer_set

# def main():
#     right_answer = 0
#     all_questions = 0

#     for name, test in tests.items():
#         print(f"\n{name}")

#         dysplay(test)

#         user_answer = input('Ввеите номер ответа: ')

#         if check_answer(user_answer, test['Правильный ответ']):
#             right_answer += 1
#         else:
#             print('')
#         all_questions += 1

#     print(f'Вы набрали {right_answer} баллов из {all_questions}.')

# main()

# # ЗАДАНИЕ 1
# 2
# a, b = map(int, input().split())
# k = 0
# n = 0
# while n < abs(b):
#     k += a
#     n +=1
# if b < 0:
#     print(-k)
# else:
#     print(k)

# # 4
# N = int(input())
# v = 0
# x = 0
# while v < N:
#     x +=2
#     print(x)
#     v+=1

# # 5
# a = int(input('Введите натуральное число: '))
# b = int(input('Введите натуральное число: ')) 
# for i in range(a,b+1):
#     print(f'{i} * {i} = {i**2}')

# # 6
# a = int(input('Введите натуральное число: '))
# b = int(input('Введите натуральное число: ')) 
# s_kv = 0
# for i in range(a,b+1):
#     s_kv += i**2
# print(s_kv)

# # 7

# N = int(input('Введите натуральное число: '))
# r_n = []
# for i in range(N):
#     r_n.append(random.randint(1,100))
# print(*r_n)
# # Когда вы запускаете программу несколько раз,
# # вы заметите, что каждый раз генерируются разные наборы псевдослучайных чисел. 
# # Это происходит потому, что функция random.randint() использует генератор псевдослучайных чисел, 
# # который основан на алгоритмах, создающих последовательности чисел, 
# # которые выглядят случайными.

# 8
# N = int(input('Введите натуральное число: '))
# for i in range(1,N+1):
#     n_s = str(i)
#     d = True
#     for dig in n_s:
#         dig_i = int(dig)
#         if dig_i == 0 or i % dig_i != 0:
#             d = False
#             break
#     if d:
#         print(i)

# # 9 
# import random
# N_v = [10, 100, 1000, 10000]
# for N in N_v:
#     r_n = [random.uniform(0, 1) for _ in range(N)]
#     c_0_25 = 0
#     c_25_50 = 0
#     c_50_75 = 0
#     c_75_100 = 0
#     for n in r_n:
#         if 0 <= n < 0.25:
#             c_0_25 += 1
#         elif 0.25 <= n < 0.5:
#             c_25_50 += 1
#         elif 0.5 <= n < 0.75:
#             c_50_75 += 1
#         elif 0.75 <= n <= 1:
#             c_75_100 += 1
#     print(f"N = {N}:")
#     print(f"Количество чисел в [0; 0.25): {c_0_25}")
#     print(f"Количество чисел в [0.25; 0.5): {c_25_50}")
#     print(f"Количество чисел в [0.5; 0.75): {c_50_75}")
#     print(f"Количество чисел в [0.75; 1): {c_75_100}")
#     print()

# # 10 
# for i in range(10000, 100000):
#     if i % 133 == 125 and i % 134 == 111:
#         print(i)

# # 11
# print("Трехзначные числа Армстронга:")
# for n in range(100, 1000):
#     a = n // 100         
#     b = (n // 10) % 10    
#     c = n % 10            
#     if (a ** 3 + b ** 3 + c ** 3) == n:
#         print(n)
# print("Четырехзначные числа Армстронга:")
# for n in range(1000, 10000):
#     a = n // 1000         
#     b = (n // 100) % 10    
#     c = (n // 10) % 10     
#     d = n % 10             
#     if (a ** 4 + b ** 4 + c ** 4 + d ** 4) == n:
#         print(n)

# # 12
# N = int(input("Введите натуральное число N: "))
# print(f"Автоморфные числа, не превосходящие {N}:")
# for n in range(1, N + 1):
#     sq = n * n
#     if str(sq).endswith(str(n)):
#         print(n)

# # 13
# n = input("Введите число: ")
# c_d = 0  
# for d in n:
#     if d.isdigit() and int(d) % 2 == 0:
#         c_d += 1 
# print(f"Количество четных цифр в числе {n}: {c_d}")

# # 14
# n = input("Введите число: ")
# sum_of_digits = 0
# for dig in n:
#     if dig.isdigit():
#         sum_of_digits += int(dig)
# print(f"Сумма цифр в числе {n}: {sum_of_digits}")

# # 15
# n = input("Введите число: ")
# h_a_d = False
# for i in range(len(n) - 1):
#     if n[i] == n[i + 1]:
#         h_a_d = True
#         break 
# if h_a_d:
#     print("В числе есть две одинаковые цифры, стоящие рядом.")
# else:
#     print("В числе нет двух одинаковых цифр, стоящих рядом.")

# # 16
# n = input("Введите число: ")
# i_s_d = True
# if len(n) > 0:
#     f_d = n[0]
#     for dig in n:
#         if dig != f_d:
#             i_s_d = False
#             break 
# if i_s_d:
#     print("Число состоит из одинаковых цифр.")
# else:
#     print("Число не состоит из одинаковых цифр.")

# # 17
# a = int(input("Введите первое натуральное число: "))
# b = int(input("Введите второе натуральное число: "))
# if a <= 0 or b <= 0:
#     print("Оба числа должны быть натуральными.")
# else:
#     while a != 0 and b != 0:
#         if a > b:
#             a = a - b 
#         else:
#             b = b - a  
#     gcd = a if a != 0 else b
#     print("Наибольший общий делитель:", gcd)

# # 18
# n = input("Введите число: ")
# u_d = set()
# h_d = False
# for dig in n:
#         if dig in u_d:
#             h_d = True
#             break
#         else:
#             u_d.add(dig) 
# if h_d:
#     print("Число содержит по крайней мере две одинаковых цифры.")
# else:
#     print("Число не содержит одинаковых цифр.")

# # 19
# ex = 10
# while ex >= 2:
#     if ex % 2 == 0:
#         print(2 ** ex)
#     ex -= 1


# for ex in range(10, 1, -1):
#     if ex % 2 == 0:
#         print(2 ** ex)

# # 20
# n1 = int(input("Введите первое число: "))
# n2 = int(input("Введите второе число: "))
# if n1 < n2:
#     n1, n2 = n2, n1
# while n2 != 0:
#     r = n1 % n2  
#     n1 = n2              
#     n2 = r
# print(f"Наибольший общий делитель = {n1}")

# # 21
# # Модифицированный Евклид
# n1 = int(input("Введите первое число: "))
# n2 = int(input("Введите второе число: "))
# if n1 < n2:
#     n1, n2 = n2, n1
# s_m= 0 
# while n2 != 0:
#     r = n1 % n2  
#     n1 = n2              
#     n2 = r
#     s_m += 1
# print(f"Наибольший общий делитель (модифицированный) = {n1}")
# print(f"Количество шагов (модифицированный) = {s_m}")

# # Классический алгоритм Евклида
# n1 = int(input("Введите первое число для классического алгоритма: "))
# n2 = int(input("Введите второе число для классического алгоритма: "))
# if n1 < n2:
#     n1, n2 = n2, n1
# s_c = 0 
# while n2 != 0:
#     n1, n2 = n2, n1 % n2
#     s_c += 1  
# print(f"Наибольший общий делитель (классический) = {n1}")
# print(f"Количество шагов (классический) = {s_c}")

# # 22
# s = 0
# p = 1
# for i in range(10):
#     a = int(input(''))
#     s += a
#     p *= a
# print(s,p)

# 23
# s = 0
# a = int(input(''))
# while a != 0:
#     s += a
#     a = int(input(''))
# print(s)

# # 24
# s = []
# a = int(input(''))
# while a != 0:
#     s.append(a)
#     a = int(input(''))
# print(max(s), min(s))