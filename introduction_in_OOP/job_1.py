class Bottle:
    def __init__(self, color, value):
        self.color = color
        self.value = value


bottle_1 = Bottle('Красная', 0.7)
bottle_2 = Bottle('Белая', 0.3)
bottle_3 = Bottle('Черная', 1.0)

print(bottle_1.color, bottle_1.value)
print(bottle_2.color, bottle_2.value)
print(bottle_3.color, bottle_3.value)