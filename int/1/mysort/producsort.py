"""
    Сортировка строки продукционными правилами
"""



from pprint import pprint
from colored import (
    stylize,
    fg,
)



class ProducSort:
    """
        Класс продукционной сортировки строки
    """


    def __init__(self, sequence, rules):
        """
            Задание последовательности,продукционных правил
        """
        self.sequence = sequence
        self.rules = rules
        self._clear_tree()


    def add_rule(self, source, result):
        """
            Добавление продукционного правила
        """
        self.rules[source] = result
        self._clear_tree()


    def del_rule(self, source):
        """
            Удаление продукционного правила
        """
        del self.rules[source]
        self._clear_tree()


    def set_sequence(self, sequence):
        """
            Задание сортируемой последовательности
        """
        self.sequence = sequence
        self._clear_tree()


    def sort(self):
        """
            Сортировка последовательности и построение дерева
        """
        self._clear_tree()
        self._build_tree(self.tree)


    def print_tree(self):
        """
            Вывод результирующего дерева
        """
        pprint(self.tree)


    def print_colored_tree(self):
        """
            Вывод цветного графа
        """
        def print_node(node, depth=0):
            is_end = node["next"] is None
            FG_NUM = 214
            FG_SEQ = 125 if is_end else 69
            FG_LINE = 240
            padding_size = 4 * depth
            print("{0}{1} {2}".format(
                    stylize(" " * (padding_size) + "|" + "_" * (padding_size), fg(FG_LINE), ),
                    stylize(str(node["data"]["produc_number"]), fg(FG_NUM)),
                    stylize(node["data"]["sequence"], fg(FG_SEQ))
                    ), end="\n"
            )
            if is_end:
                return
            for child_node in node["next"]:
                print_node(child_node, depth + 1)
        print_node(self.tree)
        print()


    def _clear_tree(self):
        """
            Очистка дерева результата
        """
        self.tree = {
            "data": {
                "produc_number": 0,
                "sequence": self.sequence
            },
            "next": None
        }


    def _build_tree(self, tree):
        """
            Построение дерева результата
        """
        for number, source in enumerate(self.rules):
            if source in tree["data"]["sequence"]:
                new_sequence = tree["data"]["sequence"].replace(source, self.rules[source])
                node = {
                    "data": {
                        "produc_number": number + 1,
                        "sequence": new_sequence
                    },
                    "next": None
                }
                self._add_node(tree, node)
                self._build_tree(node)


    def _add_node(self, tree, node):
        """
            Добавление узла в дерево
        """
        if tree["next"] is None:
            tree["next"] = [node]
        else:
            tree["next"].append(node)
