 #include <stdio.h>
 #include <conio.h>
 

 //program to print largest number without conditional statements

 void main()
 {
 int x ,y ,z;
 clrscr();
 printf("Executing program to print largest number without conditional statements....\n\n Please enter 3 numbers: ");
 scanf("%d%d%d",&x,&y,&z);
 switch(x>y && x>z)
 {
    case 1:
    printf("The largest number is %d",x);
    break;
    
    case 0:
    switch(y>z)
    {
       case 1:
       printf("The largest number is %d",y);
       break;
      
       case 0:
       printf("The largest number is %d",z);
       break;
    }
    break;
}
getch();
}
