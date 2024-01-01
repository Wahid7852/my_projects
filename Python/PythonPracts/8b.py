try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("You must enter a number!")
except:
    print("Something went wrong!")
