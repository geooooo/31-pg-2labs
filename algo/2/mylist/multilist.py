"""
    Реализация многосвязного списка
"""



from copy import deepcopy as copy
from .linearlist import LinearList



class MultiListException(Exception):
    pass



# Связь между элементами списка
Link = {
    "prev": None,
    "next": None
}

# Элемент многосвязного списка
MultiListElement = {
    "value": None,
    "id": None,
    "ptr": {
        "all": copy(Link)
    }
}

# Дескриптор
Descriptor = {
    "first": None,
    "last": None
}



class MultiList:

    def __init__(self, groups=["all"]):
        """
            Инициализация списка
            groups - список групп ссылок
        """
        if "all" not in groups:
            groups.append("all")
        self._groups = groups
        self.clear()


    def __len__(self):
        """
            Возвращает количество элементов в списке
        """
        return self._count


    def __getitem__(self, id):
        """
            Возвращает элемент списка по индексу
        """
        return self._get_element_by_id(id)["value"]


    def get_list_by_groups(self, groups):
        """
            Получение элементов в виде односвзного списка,
            которые входят в указанные группы
        """
        linear_list = LinearList()
        ptr = self._descriptors["all"]["first"]
        while ptr:
            for group in groups:
                if group not in ptr["ptr"]:
                    break
            else:
                linear_list.insert({
                    "id": ptr["id"],
                    "value": ptr["value"]
                })
            ptr = ptr["ptr"]["all"]["next"]
        return linear_list


    def insert(self, value, groups=["all"]):
        """
            Вставка значения в указанную группу списка
        """
        if "all" not in groups:
            groups.append("all")
        new_element = self._createElement(value, groups)
        for group in groups:
            self._insert(new_element, group)
        self._count += 1


    def clear(self):
        """
            Очистка списка
        """
        self._descriptors = dict()
        for group in self._groups:
            self._descriptors[group] = copy(Descriptor)
        self._id = 0
        self._count = 0


    def delete(self, id):
        """
            Удаление элемента списка по индексу
        """
        element = self._get_element_by_id(id)
        self._delete(element)
        self._count -= 1


    def is_empty(self):
        """
            Проверка списка на пустоту
        """
        return len(self) == 0


    def _createElement(self, value, groups):
        """
            Создание нового элемента
        """
        element = copy(MultiListElement)
        element["value"] = value
        element["id"] = self._id
        for group in groups:
            if group not in self._descriptors:
                # Запрет создания новых групп ссылок
                raise MultiListException("Undefined link group '{}'!".format(group))
            element["ptr"][group] = copy(Link)
        self._id += 1
        return element


    def _insert(self, element, group):
        """
            Вставка сформированного элемента в список
            и перестановка указателей
        """
        if not self._descriptors[group]["first"]:
            # Если список группы пуст
            self._descriptors[group]["last"] = element
            self._descriptors[group]["first"] = element
        else:
            last = self._descriptors[group]["last"]
            last["ptr"][group]["next"] = element
            self._descriptors[group]["last"] = element
            element["ptr"][group]["prev"] = last


    def _delete(self, element):
        """
            Удаление элемента из всего списка и всех его групп
        """
        for group in element["ptr"]:
            prev_element = element["ptr"][group]["prev"]
            next_element = element["ptr"][group]["next"]
            if not prev_element and not next_element:
                continue
            elif not prev_element:
                next_element["ptr"][group]["prev"] = None
            elif not next_element:
                prev_element["ptr"][group]["next"] = None
            else:
                prev_element["ptr"][group]["next"] = next_element
        # Удаление из таблицы дескрипторов
        for group in self._descriptors:
            if self._descriptors[group]["first"] is element:
                self._descriptors[group]["first"] = self._descriptors[group]["first"]["ptr"][group]["next"]
            if self._descriptors[group]["last"] is element:
                self._descriptors[group]["last"] = self._descriptors[group]["last"]["ptr"][group]["prev"]


    def _get_element_by_id(self, id):
        """
            Найти элемент по его индексу в списке
        """
        ptr = self._descriptors["all"]["first"]
        while ptr:
            if ptr["id"] == id:
                break
            ptr = ptr["ptr"]["all"]["next"]
        else:
            raise MultiListException("Undefined id '{}' !".format(id))
        return ptr
