class Bottle():
    color = "цвет"
    contains = "объем"

    def __init__(self):
        self.contains = 0

    def get_contains(self):
        return self.contains

    def fill(self, volume):
        self.contains += volume

bottle_1 = Bottle()
bottle_2 = Bottle()
bottle_1.color = "красная"
bottle_2.color = "белая"

print(bottle_1.color, bottle_1.get_contains())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_contains())
print(bottle_2.color, bottle_2.get_contains())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_contains())