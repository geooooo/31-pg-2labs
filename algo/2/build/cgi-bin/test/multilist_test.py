import sys
sys.path.append("/home/geo/Документы/31-pg-2labs/algo/2")

from unittest import TestCase
from mylist.multilist import MultiList



class TestMultiList(TestCase):

    def setUp(self):
        self.la = [1, 2]
        self.lb = [3]
        self.lc = []
        self.ll = self.la + self.lb + self.lc
        self.l = MultiList(["a", "b", "c"])
        for a in self.la:
            self.l.insert(a, ["a"])
        for b in self.lb:
            self.l.insert(b, ["b"])
        for c in self.lc:
            self.l.insert(c, ["c"])


    def test__init__(self):
        for a1, a2 in zip(self.ll, self.l.get_list_by_groups("all")):
            self.assertEqual(a1, a2["value"])
        for a1, a2 in zip(self.la, self.l.get_list_by_groups("a")):
            self.assertEqual(a1, a2["value"])
        for b1, b2 in zip(self.lb, self.l.get_list_by_groups("b")):
            self.assertEqual(b1, b2["value"])
        for c1, c2 in zip(self.lc, self.l.get_list_by_groups("c")):
            self.assertEqual(c1, c2["value"])


    def test__getitem__(self):
        self.assertEqual(self.la[0], self.l[0])
        self.assertEqual(self.la[1], self.l[1])


    def test__len__(self):
        self.assertEqual(len(self.ll), len(self.l))


    def test_get_list_by_groups(self):
        for a1, a2 in zip(self.la, self.l.get_list_by_groups("a")):
            self.assertEqual(a1, a2["value"])
        for l1, l2 in zip(self.ll, self.l.get_list_by_groups("all")):
            self.assertEqual(l1, l2["value"])


    def test_insert(self):
        self.l.insert(6, ["c"])
        self.l.insert("xxx")
        self.l.insert(7, ["a", "b", "c"])
        self.l.insert(8, ["a"])
        self.assertEqual(len(self.ll)+4, len(self.l))
        self.assertEqual(self.l[0], self.ll[0])
        self.assertEqual(7, self.l[len(self.l) - 2])
        self.assertEqual(8, self.l[len(self.l) - 1])


    def test_clear(self):
        self.l.clear()
        self.assertTrue(self.l.is_empty())


    def test_is_empty(self):
        self.assertFalse(self.l.is_empty())
        self.l.clear()
        self.assertTrue(self.l.is_empty())


    def test_delete(self):
        for i in range(len(self.l)):
            self.l.delete(i)
        self.assertTrue(self.l.is_empty())
        self.assertEqual(None, self.l._descriptors["all"]["first"])
        self.assertEqual(None, self.l._descriptors["all"]["last"])
