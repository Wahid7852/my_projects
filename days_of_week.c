 #include <stdio.h>
 #include <conio.h>
 
 void main()
 {
 int aS;
 clrscr();
 printf("Executing program to print days of the week using switch case......\n Select a number between 1 - 7: ");
 scanf("%d",&aS);
 switch(aS)
 {
  case 1:
  printf(" Monday");
  break;

  case 2:
  printf(" Tuesday");
  break;

  case 3:
  printf(" Wednesday");
  break;

  case 4:
  printf(" Thursday");
  break;

  case 5:
  printf(" Friday");
  break;

  case 6:
  printf(" Saturday");
  break;
  
  case 7:
  printf(" Sunday");
  break;
  
  default:
  printf("Please enter number properly between 1 - 7.");
  break;
}
getch();
}
