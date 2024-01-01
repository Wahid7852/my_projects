def remove(list):
    list = list[1::2]
    return list

list = input("Enter a list of numbers separated by space: ")
list = list.split()
list = [int(i) for i in list]
print(remove(list))