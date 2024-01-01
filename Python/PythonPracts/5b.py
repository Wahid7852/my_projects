dict1 = {}
dict2 = {}
dict3 = {}

n = int(input('Enter the number of items in dictionary 1: '))
for i in range(n):
    key = input('Enter key : ')
    value = int(input('Enter value : '))
    dict1[key] = value

n = int(input('Enter the number of items in dictionary 2: '))
for i in range(n):
    key = input('Enter key : ')
    value = int(input('Enter value : '))
    dict2[key] = value

n = int(input('Enter the number of items in dictionary 3: '))
for i in range(n):
    key = input('Enter key : ')
    value = int(input('Enter value : '))
    dict3[key] = value
    
dict4 = {}
for d in (dict1, dict2, dict3):
    dict4.update(d)
print(dict4)