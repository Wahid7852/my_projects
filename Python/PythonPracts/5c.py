dict1 = {}
dict2 = {}

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

dict3 = {}
for d in (dict1, dict2):
    dict3.update(d)
print(dict3)

sum = 0
for i in dict3:
    sum += dict3[i]
print('Sum of all items in dictionary : ', sum)

