def clone(list):
    return list.copy()

list = input("Enter a list of numbers separated by space: ")
list = list.split()
list = [int(i) for i in list]
print(clone(list))