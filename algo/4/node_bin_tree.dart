/// Узел двоичного дерева
class NodeBinTree<T> {

    /// Значение, хранящееся в узле
    T value;
    /// Левое поддерево
    NodeBinTree left;
    /// Правое поддерево
    NodeBinTree right;
    /// Родительский узел
    NodeBinTree parent;

    /// Создание узла с заданым значением
    NodeBinTree(T this.value);

}
