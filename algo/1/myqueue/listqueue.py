from copy import copy
from .abstractqueue import AbstractQueue



class ListQueue(AbstractQueue):
    """
        Реализация очереди в виде односвязного списка
    """


    # Элемент связного списка
    _NODE = {
       "value": None,
       "next": None
    }


    def __next__(self):
        """
            Реализация протокола итерации
        """
        if self._next_i == self._cur_size:
            raise StopIteration()
        self._next_i += 1
        result = self._next_head["value"]
        self._next_head = self._next_head["next"]
        return result


    def reset(self):
        super().reset()
        self._head = self._tail = copy(self._NODE)


    def insert(self, value):
        super().insert(value)
        self._tail["value"] = value
        self._tail["next"]  = copy(self._NODE)
        self._tail = self._tail["next"]


    def delete(self):
        super().delete()
        if self._head["next"] is None:
            self._head = copy(self._NODE)
        else:
            self._head = self._head["next"]


    def get(self):
        super().get()
        return self._head["value"]
