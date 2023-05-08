#include<stdio.h>
#include<conio.h>

int checkEvenOrNot(int num)
{
    if (num % 2 == 0)
        goto even; 
    else
        goto odd; 

even:
    printf("%d is even", num);
    return 0;
odd:
    printf("%d is odd", num);
}
  
void main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    checkEvenOrNot(num);
    getch();
}
