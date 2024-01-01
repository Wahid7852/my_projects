import operator

# take value from user 
d = {}

n = int(input('Enter the number of items in dictionary : '))
for i in range(n):
    key = input('Enter key : ')
    value = int(input('Enter value : '))
    d[key] = value

print('\n Original dictionary : ', d)
sd = sorted(d.items(), key=operator.itemgetter(1))
print('\n Ascending order : ', sd)

sd = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('\n Descending order : ',sd)

