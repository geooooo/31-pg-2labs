"""
    Представление системы управления
    абитуриетами университета
"""



from copy import deepcopy as copy
import pickle
from os import path

from mylist import (
    MultiList,
    MultiListException
)



class UnivException(Exception):
    pass



# Информация о студенте
Student = {
    "lastName": None,
    "city": None,
    "groups": [],
    "scores": {
        "math": None,
        "info": None,
        "phys": None
    }
}



class Univ:
    """
        Singleton - класс, представляющий систему
        упавления абитуриентами
    """

    _CITY = "Воронеж"
    _DB_NAME = "cgi-bin/univ.db"
    _INSTANCE = None


    def __init__(self):
        """
            Инициализация
        """
        if Univ._INSTANCE:
            self = Univ._INSTANCE
        else:
            Univ._INSTANCE = self
        if path.exists(Univ._DB_NAME):
            self._load()
        else:
            self._city = Univ._CITY
            self._clear()


    def close(self):
        """
            Закрытие системы и
            запись данных из БД в файл
        """
        self._dump()


    def add_student(self, student):
        """
            Добавление абитуриента в БД системы
            student - информация о студенте
        """
        isExternal = Univ._CITY != student["city"]
        isAllHighScore = True
        for score in student["scores"]:
            if student["scores"][score] != 5:
                isAllHighScore = False
                break
        if isAllHighScore:
            student["groups"].append("isAllHighScore")
        if isExternal:
            student["groups"].append("isExternal")
        groups = student["groups"]
        del student["groups"]
        self._students.insert(student, groups)


    def delete_student(self, number):
        """
            Удаление студента из базы
            number - номер удаляемого студента
        """
        try:
            self._students.delete(number)
        except MultiListException:
            raise UnivException("Студента с номером: '{}' не существует".format(number))


    def delete_all(self):
        """
            Удаление всех данных из БД
        """
        self._clear()


    def get_students(self, groups):
        """
            Получить список студентов
            groups - группы характеристик абитуриента
        """
        if not groups:
            groups.append("all")
        return self._students.get_list_by_groups(groups)


    def _clear(self):
        """
            Очистка БД
        """
        self._students = MultiList([
            "isAllHighScore",
            "isDocHighScore",
            "isExternal",
            "isHostel"
        ])


    def _dump(self):
        """
            Сохранить БД в файл
        """
        pickle.dump({
            "students": self._students,
            "city": self._city
        }, open(Univ._DB_NAME, "wb"))


    def _load(self):
        """
            Загрузить БД из файла
        """
        data = pickle.load(open(Univ._DB_NAME, "rb"))
        self._city = data["city"]
        self._students = data["students"]


    @staticmethod
    def new_student():
        """
            Получение словаря под информацию
            о новом абитуриенте
        """
        return copy(Student)
