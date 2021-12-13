class Car:
    def __init__(self,age=1996,type='легковой',color='красный'):
        self.color=color
        self.type=type
        self.age=age

    def get_age(self):
        return f'Год вашей машины {self.age}'
    def get_type(self):
        return f'Тип вашей машины {self.type}'
    def get_color(self):
        return f'Цвет вашей машины {self.color}'
    def zapusk(self):
        return  f'Машина запущена'
    def zaglushit(self):
        return  f'Машина заглушена'

car=Car(2002,'грузовик','черный')
print(car.zapusk())
print(car.get_age())
print(car.get_color())
print(car.get_type())
print(car.zaglushit())
