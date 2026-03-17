# #1
# a = {
#     '1' : "1", '2' : "8", '3' : "27", '4' : "64", '5' : "125", '6' : "216", '7' : "343", '8' : "512", '9' : "729", '10' : "1000"
# }

# print(a.values())

#2

# pythonlist = {}

# pythonlist['p'] = 1
# pythonlist['y'] = 1
# pythonlist['t'] = 2
# pythonlist['h'] = 1
# pythonlist['o'] = 1
# pythonlist['n'] = 1
# pythonlist['l'] = 1
# pythonlist['i'] = 1
# pythonlist['s'] = 1

# print(pythonlist)

#3

# list = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# proizved = list.get('a') * list.get('b') * list.get('c')

# print(proizved)

#4

# a = [1, 2, 3, 4, 5, 6]
# b = [1, 2, 3, 4, 5, 6]
# c = {}

# for i in range(0, 6):
#     c[str(a[i])] = str(b[i])
# print(c)

# #5

# l_1 = {
#     'a': 300,
#     'b': 400
# }
# l_2 = {
#     'c': 500,
#     'd': 600
# }

# # l_1.update(l_2)
# a = {**l_1, **l_2}
# print(a)

#6

# a = {}

# name = input('Введите имя: ')
# a['Имя'] = name

# age = int(input('Сколько вам лет: '))
# a['Возраст'] = str(age)

# workplace = input('Введите место работы: ')
# a['Место работы'] = workplace

# count = int(input('Сколько ЯП вы знаете: '))
# l = []
# for i in range(1, count + 1):
#     lang = input('Название ЯП: ')
#     l.append(lang)
# a['Языки Программироварния'] = l

# print(a.get('Имя'), '\n', a.get('Возраст'), '\n', a.get('Место работы'), '\n', a.get('Языки Программироварния'))

#7

# people = [
#     {'name': 'Tom', 'age': 19, 'company': 'КГАСУ', 'languages': ['Python', 'JavaScript']},
#     {'name': 'Bob', 'age': 22, 'company': 'КНИТУ-КХТИ', 'languages': ['Python', 'C++', 'C#']},
#     {'name': 'Sam', 'age': 25, 'company': 'КНИТУ-КАИ', 'languages': ['Python', 'Java']}
# ]
# for i in people:
#     name = i['name']
#     last_language = i['languages'][-1]
#     print(f"Name: {name} \nLanguage: {last_language}")
