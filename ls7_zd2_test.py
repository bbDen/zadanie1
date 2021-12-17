import unittest
from ls7_zd2 import changeWord


class TestchangeWord(unittest.TestCase):
    def setUp(self) -> None:
        self.stroka = ' Я не знаю что написать    потому будет простой текст '
        self.integer = 34

    def test_True(self):
        answer=changeWord(self.stroka)
        self.assertTrue(answer,'Я*не*знаю*что*написать*потому*будет*простой*текст')
    def test_value(self):
        with self.assertRaises(ValueError):
            answer=changeWord(self.integer)



