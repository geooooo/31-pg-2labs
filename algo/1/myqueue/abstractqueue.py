class AbstractQueue:
    """
        Абстрактная очередь
    """


    def __init__(self, size):
        """
            Инициализация очереди
        """
        # +1 чтобы различать при проверке
        # пустоту и переполнение очереди
        self._max_size = size
        self._cur_size = 0
        self.reset()


    def __iter__(self):
        """
            Реалиазация протокола итератора
        """
        # Номер элемента
        self._next_i = 0
        # Указатель на очередной элемент
        self._next_head = self._head
        return self


    def reset(self):
        """
            Сброс состояния очереди в исходное
        """
        self._cur_size = 0


    def is_full(self):
        """
            Проверка очереди на полное заполнение
        """
        return self._cur_size == self._max_size


    def is_empty(self):
        """
            Проверка очереди на пустоту
        """
        return self._cur_size == 0


    def insert(self, value):
        """
            Вставка значения в хвост очереди
        """
        if self.is_full():
            raise Exception("Queue is full !")
        self._cur_size += 1


    def delete(self):
        """
            Удаление элемента из головы очереди
        """
        if self.is_empty():
            raise Exception("Queue is empty !")
        self._cur_size -= 1


    def get(self):
        """
            Получение значения из головы очереди
        """
        if self.is_empty():
            raise Exception("Queue is empty !")
