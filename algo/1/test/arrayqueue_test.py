import sys
sys.path.append("/home/geo/Документы/31-pg-2labs/algo/1")

from unittest import TestCase
from myqueue import ArrayQueue



class TestArrayQueue(TestCase):

    def setUp(self):
        self.qsize = 5
        self.q = ArrayQueue(self.qsize)


    def test_reset(self):
        for value in range(self.qsize):
            self.q.insert(value)
        self.q.reset()
        self.assertTrue(self.q.is_empty())


    def test_insert(self):
        for value in range(self.qsize):
            self.q.insert(value)
        with self.assertRaises(Exception):
            self.q.insert(123)
        self.q.delete()
        self.q.insert(123)
        with self.assertRaises(Exception):
            self.q.insert(456)


    def test_delete(self):
        with self.assertRaises(Exception):
            self.q.delete()
        for value in range(self.qsize):
            self.q.insert(value)
        for _ in range(self.qsize):
            self.q.delete()
        with self.assertRaises(Exception):
            self.q.delete()


    def test_get(self):
        # Базовый случай
        with self.assertRaises(Exception):
            self.q.get()
        self.q.insert(1)
        self.q.insert(2)
        self.q.insert(3)
        self.assertEqual(self.q.get(), 1)
        self.q.delete()
        self.assertEqual(self.q.get(), 2)
        self.q.delete()
        self.assertEqual(self.q.get(), 3)
        self.q.delete()
        with self.assertRaises(Exception):
            self.q.get()
        # Случай когда tail < head
        for value in range(self.qsize):
            self.q.insert(value)
        self.q.delete()
        self.q.delete()
        self.q.insert(10)
        self.q.insert(11)
        self.q.delete()
        self.q.delete()
        self.q.delete()
        self.assertEqual(self.q.get(), 10)
        self.q.delete()
        self.assertEqual(self.q.get(), 11)
        self.q.delete()
        with self.assertRaises(Exception):
            self.q.get()


    def test_is_full(self):
        self.assertFalse(self.q.is_full())
        for value in range(self.qsize):
            self.q.insert(value)
        self.assertTrue(self.q.is_full())


    def test_empty(self):
        self.assertTrue(self.q.is_empty())
        self.q.insert(1)
        self.assertFalse(self.q.is_empty())


    def test_iterable_(self):
        values = [value for value in range(self.qsize)]
        for value in values:
            self.q.insert(value)
        for valueq, value0 in zip(self.q, values):
            self.assertEqual(value0, valueq)
