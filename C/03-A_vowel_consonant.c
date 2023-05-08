 #include <stdio.h>
 #include <conio.h>
 
 void main()
 {
 char c;
 clrscr();
 printf("Executing program to differ between vowel and consonant....\n Please enter a character: ");
 scanf("%c", &c);

 if(c=='a'||c=='A'||c=='e'||c=='E'||c=='i'||c=='I'||c=='o'||c=='O'||c=='u'||c=='U')
  {
   printf(" Provided character %c is a vowel",c);
  }
 else
  {
   printf(" Provided character %c is a consonant",c);
  }
 
 getch();
 }
