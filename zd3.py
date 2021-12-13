class Math:
    def init(self, a, b):
        self.a = a if isinstance(a, (int, float)) else 1
        self.b = b if isinstance(b, (int, float)) else 1

    def plus(self):
        return self.a + self.b

    def delenie(self):
        if self.b == 0:
            return 'Делить на 0 нельзя'
        else:
            return self.a / self.b

    def minus(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b


math = Math(1, 4)
print(math.delenie())
print(math.minus())
print(math.multiply())
print(math.plus())