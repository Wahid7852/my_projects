#include<stdio.h>
#include<conio.h>

struct stdent{
char name[30];
int roll;
} st[10];

void main() 
{
printf("Please enter below information:\n");
int i;

for (i = 0; i < 10; ++i) 
    { 
        printf("Enter student name:");
        scanf("%s", &st[i].name);

        printf("Enter student roll number: ");
        scanf("%d", &st[i].roll);
    }

printf("\nDisplaying stdent Information:\n\n");

for (i = 0; i < 10; ++i) 
    { 
        printf("Name: %s\n", st[i].name);
        printf("Roll number: %d\n", st[i].roll);
    }
getch();
}