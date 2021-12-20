import unittest
from zd5_ls7 import find_sum


class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        self.num = 35372
        self.str_ = 'не число'

    def test_value(self):
        answer = find_sum(self.num)
        self.assertTrue(answer, 20)

    def test_error(self):
        answer = find_sum(self.str_)
        self.assertTrue(answer, 'Вы ввели неверное значение')
