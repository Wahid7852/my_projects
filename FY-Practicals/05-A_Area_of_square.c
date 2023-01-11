#include<stdio.h>
#include<conio.h>

void main()
{
    int side, area;
    printf("Enter side of square: ");
    scanf("%d", &side);
    area = side * side;
    printf("Area of square is %d", area);
    getch();
}