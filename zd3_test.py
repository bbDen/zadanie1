import unittest
from zadacha_1.zadachi.zd3 import Math


class TestMath(unittest.TestCase):
    def test_delenie(self):
        math = Math(1, 4)
        answer = math.delenie()
        self.assertEqual(answer, 0.25)

    def test_plus(self):
        math = Math(1, 4)
        answer = math.plus()
        self.assertEqual(answer, 5)

    def test_multiply(self):
        math = Math(1, 4)
        answer = math.multiply()
        self.assertEqual(answer, 4)

    def test_minus(self):
        math = Math(1, 4)
        answer = math.minus()
        self.assertEqual(answer, -3)