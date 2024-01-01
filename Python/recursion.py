def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)
    
print(sum(5))

# here p is principal, n is number of years and Interest is assumed to be  10% so 1 + 10/100 i.e 1.1
def ci(p,n):
    if n == 1:
        return p*1.1
    else:
        return ci(p,n-1)*1.1

print(ci(2000,2))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))