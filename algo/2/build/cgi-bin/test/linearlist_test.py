import sys
sys.path.append("/home/geo/Документы/31-pg-2labs/algo/2")

from unittest import TestCase
from mylist.linearlist import LinearList



class TestLinearList(TestCase):

    def setUp(self):
        self.ls = [1, 2, 3, 4, 5]
        self.l = LinearList(self.ls)


    def test__init__(self):
        # Список не инициализируется при создании
        l = LinearList()
        self.assertTrue(l.is_empty())
        # Прогон с некоторыми последовательностями
        # в качестве инициализатора
        # строка
        ls = "string"
        l = LinearList(ls)
        for l1, l2 in zip(ls, l):
            self.assertEqual(l1, l2)
        # список из всякой всячины
        ls = [1, 2, "string", {1, 2}, {"a":"b"}]
        l = LinearList(ls)
        for l1, l2 in zip(ls, l):
            self.assertEqual(l1, l2)


    def test__len__(self):
        self.assertEqual(len(self.ls), len(self.l))
        self.l.insert("value")
        self.l.delete(0)
        self.assertEqual(len(self.ls), len(self.l))


    def test__iter__(self):
        for l1, l2 in zip(self.ls, self.l):
            self.assertEqual(l1, l2)


    def test__getitem__(self):
        for i in range(len(self.l)):
            self.assertEqual(self.ls[i], self.l[i])


    def test_clear(self):
        self.l.clear()
        self.assertTrue(self.l.is_empty())


    def test_is_empty(self):
        # Список содержит значения
        self.assertFalse(self.l.is_empty())
        # Список без значений
        self.l.clear()
        self.assertTrue(self.l.is_empty())


    def test_insert(self):
        self.l.insert("ok")
        self.assertEqual(self.l[len(self.l) - 1], "ok")
        self.l.insert(123)
        self.assertEqual(self.l[len(self.l) - 1], 123)
        self.assertEqual(self.l[len(self.l) - 2], "ok")
        for l1, l2 in zip(self.ls, self.l):
            self.assertEqual(l1, l2)


    def test_delete(self):
        for _ in self.l:
            self.l.delete(0)
        self.assertTrue(self.l.is_empty())
