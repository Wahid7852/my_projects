def fibo(n):
    a, b = 0, 1
    for i in range(n):
        for j in range(i + 1):
            print(a, end=' ')
            a, b = b, a + b
        print()

n=int(input("enter the number of terms / rows : "))
fibo(n)
