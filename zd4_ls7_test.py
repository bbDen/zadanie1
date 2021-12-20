# ['asdasdasdaszzz', 'dz21.py', 'dz2_1.py', 'dz2_2.py', 'formula.xlsx', 'lab8.zip', 'ls2.py', 'ls4-test.py', 'ls4.py', 'ls5.py', 'ls6.py', 'ls7.py', 'main.py', 'rectangles.py']
import unittest
from zd4_ls7 import file_names


class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        self.file_dir = '/Users/danny/Desktop/mOD'

    def test_true_value(self):
        answer=file_names(self.file_dir)
        self.assertTrue(answer, ['asdasdasdaszzz', 'dz21.py', 'dz2_1.py', 'dz2_2.py', 'formula.xlsx', 'lab8.zip', 'ls2.py', 'ls4-test.py', 'ls4.py', 'ls5.py', 'ls6.py', 'ls7.py', 'main.py', 'rectangles.py'])
