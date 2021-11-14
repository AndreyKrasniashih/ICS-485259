class Venicle():
    def method(self, x, y,c):
        self.x = x
        self.y = y
        self.c = c
        print(self.x,self.y, self.c)
class AirCraft(Venicle):
    def child_method(self, x, y):
        self.x = x
        self.y = y
        print(self.x, self.y)

class Ship(Venicle):
    def child_method2(self, c, y):
        self.c = c
        self.y = y
        print(self.c, self.y) 

a=AirCraft()
a.child_method('20m', '400 passengers')
b = Ship()
b.child_method2('Los-Angelos', '1200 passengers')               
