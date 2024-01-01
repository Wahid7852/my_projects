import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = datetime.datetime.now().year
print("Hello " + name + ", you will turn 100 years old in " + str(year + 100 - age))
