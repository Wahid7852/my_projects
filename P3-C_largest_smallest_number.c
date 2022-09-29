 #include <stdio.h>
 #include <conio.h>
 
 void main()
 {
 int x ,y ,z;
 clrscr();
 printf("Executing program to print largest number without conditional statements....\n\n Please enter 3 numbers: ");
 scanf("%d%d%d",&x,&y,&z);

 switch(x>y)
 {
  case 1:
  printf("%d is the largest number",x);
  break;

  case 2:
  printf("%d is the largest number",y);
  break;

  default:
  printf("%d is the largest number",z);
  break;
}
getch();
}
