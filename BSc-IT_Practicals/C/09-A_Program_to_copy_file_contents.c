//program to copy contents of one file to another file 
#include <stdio.h>
#include <conio.h>
void main()
{
    FILE *fp1, *fp2;
    char ch;
    fp1 = fopen("file1.txt", "r");
    fp2 = fopen("file2.txt", "w");
    while (1)
    {
        ch = fgetc(fp1);
        if (ch == EOF)
            break;
        else
            fputc(ch, fp2);
    }
    fclose(fp1);
    fclose(fp2);
    printf("File copied successfully");
    getch();
}