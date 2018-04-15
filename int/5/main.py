"""
    Экспертная система подбора
    ВУЗа в городе Орле
"""

# База фактов

facts = [
    {
        "univ": "огу",
        "dest": "математика",
        "is_doc_high_score": False,
        "is_high_strength":  False,
        "min_score_math": 70,
        "min_score_phys": 30,
        "min_score_rus":  30,
        "min_score_eng":  30,
        "min_score_info": 0,
        "min_score_soc":  0,
    },
    {
        "univ": "огу",
        "dest": "физика",
        "is_doc_high_score": True,
        "is_high_strength":  False,
        "min_score_math": 60,
        "min_score_phys": 70,
        "min_score_rus":  30,
        "min_score_eng":  0,
        "min_score_info": 30,
        "min_score_soc":  0,
    },
    {
        "univ": "огу",
        "dest": "информатика",
        "is_doc_high_score": False,
        "is_high_strength":  False,
        "min_score_math": 50,
        "min_score_phys": 0,
        "min_score_rus":  30,
        "min_score_eng":  40,
        "min_score_info": 70,
        "min_score_soc":  0,
    },
    {
        "univ": "огу",
        "dest": "архитектура",
        "is_doc_high_score": True,
        "is_high_strength":  False,
        "min_score_math": 50,
        "min_score_phys": 50,
        "min_score_rus":  50,
        "min_score_eng":  50,
        "min_score_info": 0,
        "min_score_soc":  20,
    },
    {
        "univ": "фсо",
        "dest": "автоматизированные системы",
        "is_doc_high_score": False,
        "is_high_strength":  True,
        "min_score_math": 60,
        "min_score_phys": 60,
        "min_score_rus":  40,
        "min_score_eng":  0,
        "min_score_info": 40,
        "min_score_soc":  0,
    },
    {
        "univ": "фсо",
        "dest": "информационная безопасность",
        "is_doc_high_score": True,
        "is_high_strength":  True,
        "min_score_math": 80,
        "min_score_phys": 40,
        "min_score_rus":  40,
        "min_score_eng":  40,
        "min_score_info": 60,
        "min_score_soc":  0,
    },
    {
        "univ": "фсо",
        "dest": "сети и телекоммуникации",
        "is_doc_high_score": False,
        "is_high_strength":  False,
        "min_score_math": 80,
        "min_score_phys": 80,
        "min_score_rus":  50,
        "min_score_eng":  0,
        "min_score_info": 30,
        "min_score_soc":  0,
    },
    {
        "univ": "фсо",
        "dest": "охрана",
        "is_doc_high_score": False,
        "is_high_strength":  True,
        "min_score_math": 50,
        "min_score_phys": 0,
        "min_score_rus":  40,
        "min_score_eng":  30,
        "min_score_info": 0,
        "min_score_soc":  30,
    },
    {
        "univ": "фсо",
        "dest": "охрана",
        "is_doc_high_score": True,
        "is_high_strength":  True,
        "min_score_math": 70,
        "min_score_phys": 70,
        "min_score_rus":  30,
        "min_score_eng":  0,
        "min_score_info": 40,
        "min_score_soc":  0,
    },
    {
        "univ": "огуэт",
        "dest": "экономика",
        "is_doc_high_score": False,
        "is_high_strength":  False,
        "min_score_math": 50,
        "min_score_phys": 0,
        "min_score_rus":  50,
        "min_score_eng":  30,
        "min_score_info": 20,
        "min_score_soc":  20,
    },
    {
        "univ": "огуэт",
        "dest": "информатика",
        "is_doc_high_score": True,
        "is_high_strength":  False,
        "min_score_math": 50,
        "min_score_phys": 0,
        "min_score_rus":  50,
        "min_score_eng":  50,
        "min_score_info": 50,
        "min_score_soc":  50,
    },
    {
        "univ": "огуэт",
        "dest": "менеджмент",
        "is_doc_high_score": True,
        "is_high_strength":  False,
        "min_score_math": 60,
        "min_score_phys": 0,
        "min_score_rus":  30,
        "min_score_eng":  0,
        "min_score_info": 0,
        "min_score_soc":  60,
    },
    {
        "univ": "огуэт",
        "dest": "управление",
        "is_doc_high_score": True,
        "is_high_strength":  True,
        "min_score_math": 70,
        "min_score_phys": 0,
        "min_score_rus":  80,
        "min_score_eng":  60,
        "min_score_info": 20,
        "min_score_soc":  80,
    },
]

# База правил

def min_score_math(desc, fact):
    return desc["score_math"] >= fact["min_score_math"]

def min_score_phys(desc, fact):
    return desc["score_phys"] >= fact["min_score_phys"]

def min_score_info(desc, fact):
    return desc["score_info"] >= fact["min_score_info"]

def min_score_soc(desc, fact):
    return desc["score_soc"] >= fact["min_score_soc"]

def min_score_rus(desc, fact):
    return desc["score_rus"] >= fact["min_score_rus"]

def min_score_eng(desc, fact):
    return desc["score_eng"] >= fact["min_score_eng"]

def is_doc_high_score(desc, fact):
    return (fact["is_doc_high_score"] and desc["is_doc_high_score"] or
            not fact["is_doc_high_score"])

def is_high_strength(desc, fact):
    return (fact["is_high_strength"] and desc["is_high_strength"] or
           not fact["is_high_strength"])

def min_score(desc, fact):
    return (min_score_math(desc, fact) and
            min_score_phys(desc, fact) and
            min_score_rus(desc, fact)  and
            min_score_eng(desc, fact)  and
            min_score_info(desc, fact) and
            min_score_soc(desc, fact))

def is_ok(desc, fact):
    return (is_high_strength(desc, fact)  and
            is_doc_high_score(desc, fact) and
            min_score(desc, fact))

# Алгоритм подбора ВУЗа и специальности
# по входным параметрам: хорошей физ. подготовке,
# наличие золотой медали, баллы ЕГЭ по предметам

def find(desc):
    result = []
    for fact in facts:
        if is_ok(desc, fact):
            result.append(fact)
    return result

# Ввод исходных данных и запуск алгоритма

print("Вы сдадите нормы ГТО (y/n) ?")
is_hs = input().strip().lower() == "y"

print("У вас есть золотая медаль (y/n) ?")
is_dhs = input().strip().lower() == "y"

print("""
    Напишите ваши результаты по
    * математике
    * русскому
    * английскому
    * обществознанию
    * информатике
    * физике
    (от 0 до 100) через 'enter'
""")

scores = {}
scores["math"] = int(input())
scores["rus"]  = int(input())
scores["eng"]  = int(input())
scores["soc"]  = int(input())
scores["info"] = int(input())
scores["phys"] = int(input())

desc = {
    "is_doc_high_score": is_dhs,
    "is_high_strength":  is_hs,
    "score_math": scores["math"],
    "score_rus":  scores["rus"],
    "score_eng":  scores["eng"],
    "score_info": scores["info"],
    "score_soc":  scores["soc"],
    "score_phys": scores["phys"],
}

result = find(desc)
if not result:
    print("Ничего не найдено :(")
else:
    print("Возможно вам стоит взглянуть на следующие направления:")
    for i, fact in enumerate(result):
        print(f"{i + 1}: {fact['univ']} - {fact['dest']}")
