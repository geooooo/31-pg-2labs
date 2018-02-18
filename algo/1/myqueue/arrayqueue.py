from .abstractqueue import AbstractQueue



class ArrayQueue(AbstractQueue):
    """
        Реализация очереди в виде массива
    """


    def __init__(self, size):
        super().__init__(size)
        self._data = [None] * self._max_size


    def __next__(self):
        """
            Реализация протокола итерации
        """
        if self._next_i == self._cur_size:
            raise StopIteration()
        self._next_i += 1
        result = self._data[self._next_head]
        if self._next_head == (self._max_size - 1):
            self._next_head = 0
        else:
            self._next_head += 1
        return result



    def reset(self):
        super().reset()
        self._head = self._tail = 0


    def insert(self, value):
        super().insert(value)
        self._data[self._tail] = value
        self._tail = 0 if self._tail == (self._max_size - 1) else self._tail + 1


    def delete(self):
        super().delete()
        self._head = 0 if self._head == (self._max_size - 1) else self._head + 1


    def get(self):
        super().get()
        return self._data[self._head]
