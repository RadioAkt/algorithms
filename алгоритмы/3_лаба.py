from math import *
#№1
# name = input('Введите ваше имя: ')
# sname = input('Введите вашу фамилию: ')
# birthplace = input('Введите ваше место рождение: ')
# favoritemusic = input('Введите любимую музыку: ')

# print(f'Ваше имя - {name}, фамилия - {sname}')
# print(f'Ваше место рождения - {birthplace}')
# print(f'Ваша любимая музыка - {favoritemusic}')

#№2

# q = {'a' : '(\_/)', 'b' : '~#####(.)(.)', 'c' : '\#####/(*)', 'd' : '||\\""||||'}
# print('{a:^12}'.format(**q))
# print('{b}'.format(**q))
# print('{c}'.format(**q))
# print('{d:^11}'.format(**q))

#№3
# a, b = map(int, input().split())

# P = a * 2 + b * 2
# print(P)

#№4
# b, c, d = map(int, input().split())

# a = (b - c) * pow(d, 2)

# print(a)

#№5 
# countcopybook, countpencil = map(int, input('Кол-во тетрадей, карандашей ').split())
# priceC, priceP = map(float, input('Цена тетрадей, карандашей ').split())

# price = (countcopybook * priceC) + (countpencil * priceP)

# print(f'Цена тетради (руб.) - > {priceC}' "\n"
#       f'Количество тетрадей - > {countcopybook}' "\n" 
#       f'Цена карандашей (руб.) - > {priceP}' "\n" 
#       f'Количество карандашей - > {countpencil}' "\n"
#       f'Стоимость покупки: {price:.2f}')

#№6
# x, t  = map(int, input().split())

# z = ((9 * pi * t + 10 * cos(x))/(sqrt(t) - abs(sin(t)))) * exp(x)

# print(f'{z:.2f}')