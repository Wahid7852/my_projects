#include <stdio.h>
#include <conio.h>
 
void main()
{
int aIP, bIP, cIP; 
clrscr();
printf("Executing program to print Inverted Half Pyramid....\n\n Please enter desired rows: ");
scanf("%d",&cIP);

for(aIP=cIP; aIP>=1; --aIP)
{
 for(bIP=1; bIP<=aIP; --bIP)
 {
  printf("*");
 }
printf("\n");
}
getch();
}
