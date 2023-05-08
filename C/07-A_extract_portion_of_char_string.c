#include<stdio.h>
#include<conio.h>

void main()
{
    char str[100],str1[100];
    int i,j,k;
    printf("Enter a string: ");
    gets(str);
    printf("Enter the starting position: ");
    scanf("%d",&i);
    printf("Enter the ending position: ");
    scanf("%d",&j);
    k=0;
    while(i<=j)
    {
        str1[k]=str[i];
        i++;
        k++;
    }
    str1[k]='\0';
    printf("The extracted string is: %s",str1);
    getch();
}