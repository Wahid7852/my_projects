# using functions

def initialize(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C

def dot_prod(u,v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans + (u[i]*v[i])
    return ans

def row(M, i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l

def column(M, j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l

def mat_mul(A,B):
    dim = len(A)
    C = initialize(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_prod(row(A,i),column(B,j)) 
    return C

# print(initialize(3))
A=[[1,2,3],[1,2,3],[1,2,3]]
B=[[1,2,3],[1,2,3],[1,2,3]]
# print(dot_prod(x,y))
print(mat_mul(A,B))