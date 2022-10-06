#include<stdio.h>
#include<conio.h>
#include<math.h>

void main()
{
    int num;
    float sqroot;
    printf("Enter a number: ");
    scanf("%d", &num);
    sqroot = sqrt(abs(num));
    printf("Square root of %d is %f", num, sqroot);
    getch();
}