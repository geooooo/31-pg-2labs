"""
    Реализация алгоритма обратного вывода
"""



from prettyprinter import cpprint as cprint
from copy import deepcopy as copy



# Стартовое правило
GOAL = "Goal"



# Строка таблицы вывода
_BackoutTableRow = {
    "number": None,
    "memory": None,
    "conflict_set": None,
    "actived_rule_number": None,
}

# Правило вывода
_Rule = {
    "source": None,
    "result": None,
}



# Набор правил вывода
_rules = None

# Память для алгоритма вывода
_memory = None

# Результирующая таблица вывода
_table = None



def set_rules(rules):
    """
        Задание набора правил вывода
        rules - список правил {исход, результат}
    """
    global _rules
    _rules = rules
    _reset()



def add_rule(source, result):
    """
       Добавление правила вывода
    """
    global _rules
    new_rule = copy(_Rule)
    new_rule["source"] = source
    new_rule["result"] = result
    _rules.append(new_rule)
    _reset()



def del_rule(number):
    """
        Удаление правила вывода по номеру
    """
    global _rules
    del _rules[number]
    _reset()



def init_memory(data):
    """
        Инициализация памяти для алгоритма
        data - список значений в памяти
    """
    global _memory
    global _goals
    _memory = []
    _memory.extend(data)
    _goals = _memory[1:]
    _reset()



def build():
    """
        Запуск алгоритма и
        построение таблицы вывода
    """
    global _memory
    global _rules
    global _table
    global _goals
    _reset()
    conflict_set = []
    offset = 0
    number0 = 0
    while _goals:
        # Проход по всем правилам
        for number, rule in zip(range(len(_rules)), _rules):
            if _is_memory_contains(rule["result"], offset):
                conflict_set.append(number)
        actived_rule_number = conflict_set[0]
        number = actived_rule_number
        for i, source in zip(range(len(_rules[number]["source"])), _rules[number]["source"]):
            _memory.insert(offset + i + 1, source)
        row = copy(_BackoutTableRow)
        row["number"] = number0
        row["memory"] = copy(_memory)
        row["conflict_set"] = copy(conflict_set)
        row["actived_rule_number"] = actived_rule_number
        _exclude_goals(_rules[number]["source"])
        _table.append(row)
        # cprint(row)
        number0 += 1
        offset += 1
        conflict_set.pop(0)



def out():
    """
        Вывод построенной таблицы
    """
    global _table
    cprint(_table)



def _reset():
    """
        Сброс таблицы вывода
    """
    global _table
    _table = []



def _is_memory_contains(data, offset):
    """
        Проверка, содержит ли память указанные данные
    """
    global _memory
    for i in range(offset, len(_memory)-len(data)+1):
        is_ok = True
        j = i
        for k in range(len(data)):
            if _memory[j] != data[k]:
                is_ok = False
                break
            j += 1
        if is_ok:
            return True
    return False



def _exclude_goals(goals):
    """
        Исключение целей
    """
    global _goals
    for goal in goals:
        if goal in _goals:
            _goals.remove(goal)
