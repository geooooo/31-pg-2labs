/*
 * Реализация прямого вывода
 */



import "dart:io";



// Признак остановки вывода
const STOP = "goal";



// Рабочая память
final List<String> _memory = [];

// Продукционные правила
final List<Map<String, List<String>>> _rules = [];

// Результат прямого вывода
final List<Map<String, List<String>>> _resultTable = [];



/*
 * Инициализировать рабочую память
 */
void initMemory(final List<String> data) {
    for (var element in data) {
        _memory.add(element);
    }
    _resultTable.add({
        "stepNumber": "0",
        "memory": _memory.toString(),
        "conflictSet": "{}",
        "activeRuleNumber": "start"
    });
}



/*
 * Задать продукционные правила
 */
void setProducRules(final List<Map<String, List<String>>> rules) {
    for (var rule in rules) {
        _rules.add(rule);
    }
}



/*
 * Запуск процедуры прямого вывода
 */
void run() {
    Set<int> conflictSet = new Set();
    var stepNumber = 1;
    var activeRuleNumber = -1;
    var offset = 0;
    while (true) {
        if (activeRuleNumber != -1) {
            conflictSet.remove(activeRuleNumber+1);
            _memory.addAll(_rules[activeRuleNumber]["result"]);
        }
        for (var number = 0; number < _rules.length; number++) {
            if (_isMemoryContains(_rules[number]["source"], offset)) {
                activeRuleNumber = number;
                conflictSet.add(activeRuleNumber+1);
            }
        }
        offset = _memory.length;
        if (_memory[_memory.length - 1] == STOP) {
            activeRuleNumber = -1;
        }
        _resultTable.add({
            "stepNumber": stepNumber.toString(),
            "memory": _memory.toString(),
            "conflictSet": conflictSet.toString(),
            "activeRuleNumber": (activeRuleNumber != -1)? (activeRuleNumber+1).toString() : "stop"
        });
        if (_memory[_memory.length - 1] == STOP) {
            break;
        }
        stepNumber++;
    }
}



/*
 * Вывод таблицы результатов
 */
void printResultTable() {
    for (var line in _resultTable) {
        stdout.writeln(line);
    }
}



/*
 * Проверка, содержит ли память указанные данные
 */
bool _isMemoryContains(List<String> data, int offset) {
    for (var i = offset; i <= _memory.length-data.length; i++) {
        var is_ok = true;
        for (var j = i, k = 0; k < data.length; j++, k++) {
            if (_memory[j] != data[k]) {
                is_ok = false;
                break;
            }
        }
        if (is_ok) {
            return true;
        }
    }
    return false;
}
