#include<stdio.h>
#include<conio.h>

void main()
{
    int a=10, b=20, *p1, *p2, sum, sub;
    p1=&a;
    p2=&b;
    sum=*p1+*p2;
    sub=*p1-*p2;
    printf("sum is %d and subtraction is %d", sum, sub);
    getch();
}