#include<stdio.h>
#include<conio.h>

void main()
{
int  n1=0, n2=1, n3, iFibo, numFibo, 
clrscr();
printf("Program for printing fibonacci series...\n\nEnter number: ");
scanf("%d", &numFibo);

for(iFibo=2;i<numFibo;++i)
{
 n3=n1+n2;
 printf("%d",n3);
 n1=n2;
 n2=n3;
}
getch();
}
