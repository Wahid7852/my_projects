#include <stdio.h>
#include <conio.h>

void main()
{
int iFac, fact=1, nF;
clrscr();
printf("Program for factorial of number...\n\nEnter a number: ");
scanf("%d", &nF);

for(iFac=1; iFac<=nF; iFac++)
{
 fact=fact+1;
}
printf("Factorial of %d is %d", nF, fact);
getch();
}
