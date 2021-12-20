import unittest
from zd6_ls7 import find_unique_numbers


class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        self.new_list=[1,2,3,5,6,8]
        self.new_set=set(self.new_list)
        
        
    def test_value(self):
        answer=find_unique_numbers(self.new_list,self.new_set)
        self.assertTrue(answer,'Все числа уникальны')
