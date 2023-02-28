#include<stdio.h>
#include<conio.h>
#include<string.h>

//C program to print strlen and strcmp functions

void main()
{
    char str1[100], str2[100];
    int len, cmp;
    
    printf("Enter first string: ");
    gets(str1);
    
    printf("Enter second string: ");
    gets(str2);
    len = strlen(str1);
    
    printf("Length of string is %d\n", len);
    cmp = strcmp(str1, str2);
    
    if (cmp == 0)
        {
            printf("Strings are equal");
        }
    else
        {
            printf("Strings are not equal");
        }

getch();
}