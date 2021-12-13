import unittest
from zd4 import Car


class TestCar(unittest.TestCase):

    def test_start(self):
        car = Car(2002, 'грузовик', 'черный')
        answer = car.zapusk()
        self.assertEqual(answer, 'Машина запущена')

    def test_glush(self):
        car = Car(2002, 'грузовик', 'черный')
        answer = car.zaglushit()
        self.assertEqual(answer, 'Машина заглушена')

    def test_age(self):
        car = Car(2002, 'грузовик', 'черный')
        answer = car.get_age()
        self.assertEqual(answer,f'Год вашей машины {car.age}')

    def test_color(self):
        car = Car(2002, 'грузовик', 'черный')
        answer = car.get_color()
        self.assertEqual(answer, f'Цвет вашей машины {car.color}')

    def test_type(self):
        car = Car(2002, 'грузовик', 'черный')
        answer = car.get_type()
        self.assertEqual(answer, f'Тип вашей машины {car.type}')
