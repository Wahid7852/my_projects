#include<stdio.h>
#include<conio.h>

void main()
{
    int a=10;
    float b=20.5;
    char c='A';
    printf("Displaying values: \n");
    printf("value of a is %d and address of a is %u\n", a, &a);
    printf("value of b is %f and address of b is %u\n", b, &b);
    printf("value of c is %c and address of c is %u\n", c, &c);
    getch();
}

