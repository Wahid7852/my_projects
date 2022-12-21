#include<stdio.h>
#include<conio.h>
#include<math.h>

//function declaration
long int factorial (int n);
int main()
{
    int n;
    long int fact;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    //function call
    fact = factorial(n);
    printf("Factorial of %d is %ld", n, fact);
    getch();
    return 0;
}

//function definition
long int factorial (int n)
{
    if (n == 0)
        return 1;
    else
        return (n * factorial(n - 1));
}