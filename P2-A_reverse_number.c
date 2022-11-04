//P2-A, Reverse number

#include <stdio.h>
#include <conio.h>

void main()
{
int nR, reverse=0, rm;
printf("Program for reversing a number...\n\nEnter 2 digit number: ");
scanf("%d", &nR);

while(nR!=0)
{
 rm=nR%10;
 reverse=reverse*10+rm;
 nR/=10;
}

printf("Reversed Number = %d", reverse);
getch();
}
