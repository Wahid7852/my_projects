class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Child(Parent):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def display(self):
        super().display()
        print("Roll: ", self.roll)

c1 = Child("Rahul", 20, 1)
c1.display()
