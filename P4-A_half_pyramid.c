#include <stdio.h>
#include <conio.h>
 
void main()
{
int aP, bP, cP; 
clrscr();
printf("Executing program to print Half Pyramid....\n\n Please enter desired rows: ");
scanf("%d",&cP);

for(aP=1; aP<=cP; aP++)
{
 for(bP=1; bP<=aP; bP++)
 {
  printf("*");
 }
printf("\n");
}
getch();
}
