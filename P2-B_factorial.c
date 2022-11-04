#include <stdio.h>
#include <conio.h>

void main()
{
int iFac, fact=1, nF;
printf("Program for factorial of number...\n\nEnter a number: ");
scanf("%d", &nF);

for(iFac=1; iFac<=nF; iFac++)
{
 fact=fact*iFac;
}
printf("Factorial of %d is %d", nF, fact);
getch();
}
