class Numbers:
    MULTIPLIER = 2
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y
    
    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a
    
    @staticmethod
    def subtract(b, c):
        return b - c
    
    @property
    def value(self):
        return (self.x, self.y)
    
    @value.setter
    def value(self, xy):
        self.x, self.y = xy
        
    @value.deleter
    def value(self):
        del self.x
        del self.y

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
n = Numbers(a, b)
print(n.add())
print(n.multiply(3))
print(n.subtract(3, 2))
print(n.value)
n.value = (3, 2)
print(n.value)
del n.value
