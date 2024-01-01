a = input("Enter a number between 5 and 9: ")
b = 'quit'

if a != b:
    if int(a) < 5 or int(a) > 9:
        raise TypeError("Wrong number range")
else:
    print("You have entered 'quit'")