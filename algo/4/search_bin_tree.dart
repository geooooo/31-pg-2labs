import "dart:io" show File;
import "node_bin_tree.dart";


/// Поисковое двоичное дерево
class SearchBinTree {

    /// Корень дерева
    NodeBinTree<int> _root;

    /// Создание дерева на основе данных
    /// в указанном файле с именем [file_name]
    SearchBinTree(String file_name) {
        // Считывание данных из файла
        var nums = new File(file_name).readAsStringSync()
                                      .trim()
                                      .replaceAll("\n", " ")
                                      .split(" ")
                                      .map((num) => int.parse(num));
        // Формирование дерева на основе данных
        for (var num in nums) {
            this._createNodeFromData(num);
        }
    }

    /// Строковое представление дерева
    @override
    String toString() {

        // Рекурсивное преобразование текущего узла [node] в строку
        String innerToString(NodeBinTree node) {
            if (node == null) return "";
            var left_value  = "";
            var right_value = "";
            if (node.left  != null) left_value  = "(${node.left.value})";
            if (node.right != null) right_value = "(${node.right.value})";
            var result = "(${node.value})\n\tleft: ${left_value}\n\tright: ${right_value}\n";
            return result + innerToString(node.left) + innerToString(node.right);
        }

        // Рекурсивное преобразование дерева в строку
        return innerToString(this._root);
    }

    /// Удаление узла дерева по значению в узле,
    /// если такой узел имеется
    void deleteNode(int value) {

        NodeBinTree del_node;
        void innerFindNode(NodeBinTree node) {
            if (node == null) return;
            if ((node.left != null) && (node.left.value == value)) {
                del_node  = node.left;
                return;
            }
            if ((node.right != null) && (node.right.value == value)) {
                del_node  = node.right;
                return;
            }
            if ((node.right == null) && (node.left == null) && (node.value == value)) {
                del_node = node;
                return;
            }
            innerFindNode(node.left);
            innerFindNode(node.right);
        }

        NodeBinTree max_right;
        void innerFindMaxRight(NodeBinTree node) {
            if (node.right != null) innerFindMaxRight(node.right);
            else {
                max_right = node;
                return;
            }
        }

        // Поиск удаляемого узла
        innerFindNode(this._root);
        if (del_node == null) return;
        if ((del_node.right == null) && (del_node.left == null)) {
            if (del_node.parent.left  == del_node) del_node.parent.left  = null;
            if (del_node.parent.right == del_node) del_node.parent.right = null;
            return;
        }

        // // Удаление узла
        if (del_node.parent.left == del_node) {
            if ((del_node.left != null) && (del_node.right == null)) {
                del_node.parent.left = del_node.left;
                del_node.left.parent = del_node.parent;
            } else if ((del_node.left == null) && (del_node.right != null)) {
                del_node.parent.left = del_node.right;
                del_node.right.parent = del_node.parent;
            } else {
                innerFindMaxRight(del_node.left);
                max_right.parent = del_node.parent;
                max_right.parent.right = max_right;
                if (max_right != del_node.right) {
                    max_right.right = del_node.right;
                }
                max_right.left = del_node.left;
            }
        } else if (del_node.parent.right == del_node) {
            if ((del_node.left != null) && (del_node.right == null)) {
                del_node.parent.right = del_node.left;
                del_node.left.parent = del_node.parent;
            } else if ((del_node.left == null) && (del_node.right != null)) {
                del_node.parent.right = del_node.right;
                del_node.right.parent = del_node.parent;
            } else {
                innerFindMaxRight(del_node.left);
                max_right.parent = del_node.parent;
                max_right.parent.right = max_right;
                if (max_right != del_node.left) {
                    max_right.left = del_node.left;
                }
                max_right.right = del_node.right;
            }
        }
    }

    /// Получить список значений узлов, у которых количество потомков
    /// в левом поддереве отличается от количества потомков
    /// в правом поддереве на единицу,
    /// на основе рекурсивного алгоритма восходящего обхода:
    /// левое - правое - корень
    List<int> getNodesValueDifOne() {

        int innerChildNodesCount(NodeBinTree node) {
            if (node == null) return 0;
            return 1 + innerChildNodesCount(node.left) +
                       innerChildNodesCount(node.right);
        }

        var result = new List<int>();
        void inner(NodeBinTree node) {
            if (node == null) return;
            inner(node.left);
            inner(node.right);
            int lcount = innerChildNodesCount(node.left);
            int rcount = innerChildNodesCount(node.right);
            if ((lcount - rcount).abs() == 1) result.add(node.value);
        }

        inner(this._root);
        return result;
    }

    int operator [](int index) {

        // Смешанный обход: левый - корень - правый
        var nums = new List<int>();
        void innerFindAllList(NodeBinTree node) {
            if (node == null) return;
            if ((node.left == null) && (node.right == null)) {
                nums.add(node.value);
                return;
            }
            innerFindAllList(node.left);
            innerFindAllList(node.right);
        }

        innerFindAllList(this._root);
        return nums[index];
    }

    /// Определение высоты дерева
    int get height {

        // Нисходящий обход: корень - левый - правый
        int max_height = 0;
        void innerHeight(NodeBinTree node, int cur_height) {
            if (node == null) {
                if (cur_height > max_height) max_height = cur_height;
                return;
            }
            cur_height++;
            innerHeight(node.left, cur_height);
            innerHeight(node.right, cur_height);
        }

        innerHeight(this._root, 0);
        return max_height;
    }

    /// Создание нового узла дерева
    /// со значением [value]
    void _createNodeFromData(int value) {
        var new_node = new NodeBinTree<int>(value);
        if (this._root == null) {
            // Если дерево было пусто
            this._root = new_node;
        } else {
            this._appendNode(new_node);
        }
    }

    /// Добавление узла [node] в дерево
    void _appendNode(NodeBinTree node) {

        // Рекурсивная вставка узла [new_node] в узел [cur_node]
        void innerAppendNode(NodeBinTree cur_node, NodeBinTree new_node) {
            if (new_node.value < cur_node.value) {
                // идём в левое поддерево
                if (cur_node.left == null) {
                    cur_node.left = new_node;
                    new_node.parent = cur_node;
                } else {
                    innerAppendNode(cur_node.left, new_node);
                }
            } else if (new_node.value > cur_node.value) {
                // идём в правое поддерево
                if (cur_node.right == null) {
                    cur_node.right = new_node;
                    new_node.parent = cur_node;
                } else {
                    innerAppendNode(cur_node.right, new_node);
                }
            }
        }

        // Рекурсивная вставка нового узла
        innerAppendNode(this._root, node);
    }

}
