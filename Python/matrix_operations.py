a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[11,12,13],[14,15,16],[17,18,19]]
c=[[0,0,0],[0,0,0],[0,0,0]]
dim = 3

def add():
    for i in range(dim):
        for j in range(dim):
            c[i][j] = a[i][j] + b [i][j]
    print(c)        


def sub():
    for i in range(dim):
        for j in range(dim):
            if b[i][j] < a[i][j]:
                c[i][j] = a[i][j] - b[i][j]

            if b[i][j] > a[i][j]:
                c[i][j] = b[i][j] - a[i][j]

    print(c)        

def mul():
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    print(c)

add()
sub()
mul()   

# easy way to multiply matrixes lol
import numpy
X = numpy.mat(a)
Y = numpy.mat(b)
print(X*Y)
