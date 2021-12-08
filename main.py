class Soda:

    def init(self, add=None, name='Gazirovka'):
        self.add = add
        self._name = 'Gazirovka'

    def show_drink(self):
        if self.add == None:
            print('Обычная газировка')

        else:
            print(f'{self._name} with {self.add}')


soda = Soda()
soda.show_drink()