class Series:
    def __init__(self, resistors):
        self.resistors = resistors

    def get_resistance(self):
        total_resistance = sum(self.resistors)
        return total_resistance

r1 = Series([100,200,300,400,500])
print(r1.get_resistance())