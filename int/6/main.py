"""
    ЭС диагностики компьютерных неисправностей
"""


# База фактов

facts = [
    {
        "problem": 'Монитор не работает',
        "answers": [
            'Проблемы с монитором. Проверьте кабель. Исправен?',
            'Проверте наличие изображения на экране. Имеется?',
        ]
    },
    {
        "problem": 'Системный блок не включается',
        "answers": [
            'Возможны проблемы с блоком питания. Исправен?',
            'Проверте шнур в розетке. Вставлен?',
            'Проверте наличие электричества в доме. Имеется?',
        ]
    },
    {
        "problem": 'Не загружается ОС',
        "answers": [
            'Возможно, проблема с ОЗУ. Исправна?',
            'Возможно, проблема с жёстким диском. Исправен?',
            'Возможно на вашем компьютере вирус. Проверьте свой компьютер на вирусы. Компьютер чист?',
        ]
    },
    {
        "problem": 'Мышь не работает',
        "answers": [
            'Возможно, проблема с кабелем мыши. Исправен?'
        ]
    },
    {
        "problem": 'Принтер не печатает',
        "answers": [
            'Возможно не установлен драйвер принтера. Установлен?',
            'Возможно принтер не включен или отсутствует питание. Включен?'
        ]
    },
]





def add_fact(*, problem=None, answer=None):
    global facts
    if problem and not answer:
        facts.append({
            "problem": problem,
            "answers": []
        })
        return
    if not problem and answer:
        raise Exception("bad")
    for fact in facts:
        if problem == fact["problem"]:
            fact["answers"].append(answer)
            break
    else:
        facts = {
            "problem": problem,
            "answers": [answer]
        }


def del_problem(problem):
    global facts
    for i, fact in enumerate(facts):
        if problem == fact["problem"]:
            break
    else:
        i = -1
    if i != -1:
        facts.pop(i)


def del_answer_of_problem(problem, answer):
    global facts
    for fact in facts:
        if problem == fact["problem"]:
            answers = fact["answers"]
            del answers[answers.index(answer)]
            break


def print_problem_answers(problem):
    global facts
    for fact in facts:
        if problem == fact["problem"]:
            print("\n".join(fact["answers"]))
            break


def print_problems():
    global facts
    for fact in facts:
        print(fact["problem"])


def print_facts():
    global facts
    for fact in facts:
        print(f"### {fact['problem']} ###")
        print("\n".join(fact["answers"]))


def find_answer(problem):
    for fact in facts:
        if problem == fact["problem"]:
            for answer in fact["answers"]:
                print(f"{answer} y\\n")
                is_y = input().strip().lower() == "y"
                if not is_y:
                    print("Проблема найдена !")
                    break
            else:
                 print("Обратитесь в сервисный центр !")


# Старт

while True:
    print("""
        0 - выход
        1 - Добавить проблему
        2 - Добавить ответ на проблему
        3 - Удалить проблему
        4 - Удалить ответ на проблему
        5 - Вывести все факты
        6 - Вывести все проблемы
        7 - Вывести все ответы на проблему
        8 - Поиск ответа
    """)
    num = int(input().strip())
    if num == 0:
        print("Пока !")
        break
    elif num == 1:
        problem = input().strip()
        add_fact(problem=problem)
    elif num == 2:
        problem = input().strip()
        answer = input().strip()
        add_fact(problem=problem, answer=answer)
    elif num == 3:
        problem = input().strip()
        del_problem(problem)
    elif num == 4:
        problem = input().strip()
        answer  = input().strip()
        del_answer_of_problem(problem, answer)
    elif num == 5:
        print_facts()
    elif num == 6:
        print_problems()
    elif num == 7:
        problem = input().strip()
        print_problem_answers(problem)
    elif num == 8:
        problem = input().strip()
        find_answer(problem)
