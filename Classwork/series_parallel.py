class Series:
       def __init__(self, resistors):
               self.resistors = resistors
       def get_resistance(self):
               effective_r = sum(self.resistors)
               return effective_r

s = Series([100, 200])
print("Resistors in series", s.get_resistance())

class Parallel:
       def __init__(self, resistors):
               self.resistors = resistors
       def get_resistance(self):
               # you may assume two elements in the resistors list for simplicity
               effective_r = 1/(1/self.resistors[0] + 1/self.resistors[1])
               return effective_r
p = Parallel([100, 200])
print("Resistors in parallel", p.get_resistance())
                

