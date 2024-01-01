def less_than_five(list):
    for i in list:
        if i < 5:
            print(i)

list = input("Enter a list of numbers separated by space: ")
list = list.split()
list = [int(i) for i in list]
less_than_five(list)