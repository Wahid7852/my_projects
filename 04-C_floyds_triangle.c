#include <stdio.h>
#include <conio.h>
 
void main()
{
int aFL, bFL, cFL, dFL=1; 
clrscr();
printf("Executing program to print Floyd's Triangle....\n\n Please enter desired rows: ");
scanf("%d",&aFL);

for(bFL=1; bFL<=aFL;bFL++)
{
 for(cFL=1; cFL<+bFL; cFL++)
 {
  printf("%d",dFL);
  dFL++;
 }
printf("\n");
}
getch();
}
