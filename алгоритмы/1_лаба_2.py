# questions = {
#     '1':{
#         "question": "Библиотека математического модуля в Python?",
#         "options": "1. random " "2. math " "3. abs " "4. mathematic",
#         "correct_answer": [2]
#     },
#     '2':{
#         "question": "Библиотека для цветного текста в Python?",
#         "options": "1. colorist " "2. colorama " "3. colorpyt " "4. color",
#         "correct_answer": [2]
#     },
#     '3':{
#         "question": "Библиотека для псевдорандомных чисел в Python?",
#         "options": "1. math " "2. itertools " "3. random " "4. os.path",
#         "correct_answer": [3]
#     },
#     '4':{
#         "question": "Оператор вывода в Python?",
#         "options": "1. print " "2. input " "3. reversed " "4. sort",
#         "correct_answer": [1]
#     },
#     '5':{
#         "question": "Какого типа данных нет в Python?",
#         "options": "1. double " "2. integer " "3. boolean " "4. dictionary",
#         "correct_answer": [1]
#     },
# }

# def dysplay(quests):
#     print(f"Вопрос: {quests['question']}\n")

#     print(f"Варианты: {quests['options']}\n")

# def check_ans(ans, cor_ans):
#      ans_set = set(map(int, ans))

#      cor_ans_set = set(cor_ans)

#      return ans_set == cor_ans_set

# score = 0
# num_questions = 0
# for name, quest in questions.items():
#         print(f"\n{name}")

#         dysplay(quest)

#         while True: 
#             answer = input("Введите номер вашего ответа: ")
#             if check_ans(answer, quest['correct_answer']):
#                 print("Правильно!")
#                 score += 1
#             else:
#                 print("Неправильно!")
#             break
#         num_questions += 1


# print(f"\nВы заработали {score} из {num_questions} баллов.")

questions = [
    {
        "question": "Библиотека математического модуля в Python?",
        "options": ["1. random", "2. math", "3. abs", "4. mathematic"],
        "correct_answer": 2
    },
    {
        "question": "Библиотека для цветного текста в Python?",
        "options": ["1. colorist", "2. colorama", "3. colorpyt", "4. color"],
        "correct_answer": 2
    },
        {
        "question": "Библиотека для псевдорандомных чисел в Python?",
        "options": ["1. math", "2. itertools", "3. random", "4. os.path"],
        "correct_answer": 3
    },
    {
        "question": "Оператор вывода в Python?",
        "options": ["1. print", "2. input", "3. reversed", "4. sort"],
        "correct_answer": 1
    },
    {
        "question": "Какого типа данных нет в Python?",
        "options": ["1. double", "2. integer", "3. boolean", "4. dictionary"],
        "correct_answer": 1
    },
    {
        "question": "Модуль числа в Python обозначается?",
        "options": ["1. abs", "2. abc", "3. module", "4. range"],
        "correct_answer": 1
    }
]
while True:
    num_questions = int(input("Введите количество вопросов (минимум 5): "))
    if num_questions >= 5 and num_questions <= len(questions):
        break
    else:
        print("Пожалуйста, введите число от 5 до", len(questions))
score = 0
for i in range(num_questions):
    print(questions[i]["question"])
    for option in questions[i]["options"]:
        print(option)
    
while True:

        answer = int(input("Введите номер вашего ответа: "))
        if 1 <= answer <= len(questions[i]["options"]):
            if answer == questions[i]["correct_answer"]:
                print("Правильно!")
                score += 1
            else:
                print("Неправильно!")
            break
        else:
            print(f"Пожалуйста, введите число от 1 до {len(questions[i]['options'])}.")


print(f"\nВы заработали {score} из {num_questions} баллов.")