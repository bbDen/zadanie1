class Soda:

    def init(self, add=None):
        self.add = add

    def show_drink(self):
        if self.add == None:
            print('Обычная газировка')

        else:
            print(f'Газировка с {self.add}')


soda = Soda()
soda.show_drink()