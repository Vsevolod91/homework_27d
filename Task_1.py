class Bottle():
    color = "цвет"
    volume = 0.0

    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

bottle_1 = Bottle("красная", 0.7)
bottle_2 = Bottle("белая", 0.3)
bottle_3 = Bottle("черная", 0.1)

# bottle_1 = Bottle()
# bottle_2 = Bottle()
# bottle_3 = Bottle()
# setattr(bottle_1, "color", "красная")
# setattr(bottle_1, "volume", 0.7)
# setattr(bottle_2, "color", "белая")
# setattr(bottle_2, "volume", 0.3)
# setattr(bottle_3, "color", "черная")
# setattr(bottle_3, "volume", 0.1)

print(bottle_1.color, bottle_1.volume)
print(bottle_2.color, bottle_2.volume)
print(bottle_3.color, bottle_3.volume)