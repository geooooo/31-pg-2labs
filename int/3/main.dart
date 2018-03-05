import "direct_output.dart";



void main(final List<String> args) {
    // Установка стартовых данных
    initMemory(["L", "M", "N"]);
    // Установка продукционных правил
    setProducRules([
        {"source": ["G","H"], "result": ["C"]},
        {"source": ["I","K"], "result": ["D"]},
        {"source": ["L","M"], "result": ["E"]},
        {"source": ["N"], "result": ["F"]},
        {"source": ["O"], "result": ["F"]},
        {"source": ["C"], "result": ["A"]},
        {"source": ["D"], "result": ["A"]},
        {"source": ["E"], "result": ["B"]},
        {"source": ["F"], "result": ["B"]},
        {"source": ["A"], "result": [STOP]},
        {"source": ["B"], "result": [STOP]}
    ]);
    // Запус процедуры вывода
    run();
    // Вывод таблицы вывода
    printResultTable();
}
