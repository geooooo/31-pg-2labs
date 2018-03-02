"""
    Реализация односвязного списка
"""



from copy import copy



# Элемент списка
ListElement = {
    "value": None,
    "next": None
}



class LinearList:

    def __init__(self, values=None):
        """
            Инициализация списка
            values - последовательность элементов для инициализации
        """
        self.clear()
        if values:
            for value in values:
                self.insert(value)


    def __iter__(self):
        self.__iter_ptr = self._data
        return self


    def __next__(self):
        if self.__iter_ptr is None:
            raise StopIteration();
        result = self.__iter_ptr["value"]
        self.__iter_ptr = self.__iter_ptr["next"]
        return result


    def __len__(self):
        return self._count


    def __getitem__(self, index):
        """
            Получение значения элемента списка с заданым номером
        """
        ptr = self._data
        for _ in range(index):
            ptr = ptr["next"]
        return ptr["value"]


    def clear(self):
        """
            Очистка списка
        """
        self._data = None
        self._ptr_last = None
        self._count = 0


    def is_empty(self):
        """
            Проверка списка на пустоту
        """
        return len(self) == 0


    def insert(self, value):
        """
            Вставка нового элемента в конец списка
        """
        if self.is_empty():
            self._data = self._ptr_last = copy(ListElement)
            self._ptr_last["value"] = value
        else:
            self._ptr_last["next"] = copy(ListElement)
            self._ptr_last = self._ptr_last["next"]
            self._ptr_last["value"] = value
        self._count += 1


    def delete(self, index):
        """
            Удаление элемента из списка по заданому номеру
        """
        # Получение ссылки на элемент стоящий перед
        # элементом с указаным индексом
        ptr = self._data
        for _ in range(index - 1):
            ptr = ptr["next"]
        if index == 0:
            self._data = self._data["next"]
        else:
            ptr["next"] = ptr["next"]["next"]
        self._count -= 1
