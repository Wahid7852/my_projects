//P2-D, Roots of quad equation

#include<stdio.h>
#include<conio.h>
#include<math.h>

void main()
{
int aQ, bQ, cQ;
float x1,x2,dQ,dl;
clrscr();
printf("Program for Roots of Quad Equation...\n\nEnter values for a,b and c: ");
scanf("%d %d %d", &aQ, &bQ, &cQ);
dQ = bQ*bQ-4*aQ*cQ;

if (dQ=0)
{
 printf("Roots are equal\n");
 x1=(-b+sqrt(dQ)/(2*aQ);
 x2=(-b-sqrt(dQ)/(2*aQ);
}

if (dQ<0)
{
 printf("Roots are imaginary\n");
 d1=abs(dQ);
 x1=(-b+sqrt(d1)/(2*aQ);
 x2=(-b-sqrt(d1)/(2*aQ);
}

if (dQ>0)
{
 printf("Roots are real\n");
 x1=(-b+sqrt(dQ)/(2*aQ);
 x2=(-b-sqrt(dQ)/(2*aQ);
}

printf(Root x1=%f\n",x1);
printf(Root x2=%f\n",x2);
getch();
}
