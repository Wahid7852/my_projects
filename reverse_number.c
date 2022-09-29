//P2-A, Reverse number

#include <stdio.h>
#include <conio.h>

void main()
{
int nR, reverse=0, rm;
clrscr();
printf("Program for reversing a number...\n\nEnter 2 digit number: ");
scanf("%d", &nR);

while(n!=0)
{
 rm=n%10;
 reverse=reverse*10+rm;
 n/=10
}

printf("Reversed Number = %d". reverse);
getch();
}
