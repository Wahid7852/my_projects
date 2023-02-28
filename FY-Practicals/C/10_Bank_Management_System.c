#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<dos.h>
#include<time.h>

struct bank
{
char name[20];
int accno;
int balance;
char phone[10];
}b;

void addA()
{
    FILE *fp;
    char another = 'y';
    fp = fopen("bank.dat", "ab+");

    if (fp == NULL)
    {
        printf("Cannot open file");
        exit(0);
    }

    while (another == 'y')
    {
        printf("Enter name: ");
        scanf("%s", b.name);

        printf("Enter account number: ");
        scanf("%d", &b.accno);

        printf("Enter balance: ");
        scanf("%d", &b.balance);

        printf("Enter phone number: ");
        scanf("%s", b.phone);
        fwrite(&b, sizeof(b), 1, fp);

        printf("Add another record(y/n): ");
        fflush(stdin);
        another = getche();
    }
    fclose(fp);
}

void balanceA()
{
    FILE *fp;
    int accno;
    int flag = 0;

    fp = fopen("bank.dat", "rb");
    if (fp == NULL)
    {
        printf("Cannot open file");
        exit(0);
    }

    printf("Enter account number: ");
    scanf("%d", &accno);
    while (fread(&b, sizeof(b), 1, fp) == 1)
    {
        if (b.accno == accno)
        {
            printf("Name: %s", b.name);
            printf("Account number: %d", b.accno);
            printf("Balance: %d", b.balance);
            printf("Phone number: %s", b.phone);
            flag = 1;
        }
    }

    if (flag == 0)
        printf("Record not found");
    fclose(fp);
}

void closeACC()
{
    FILE *fp, *ft;
    int accno;
    int flag = 0;

    fp = fopen("bank.dat", "rb");
    if (fp == NULL)
    {
        printf("Cannot open file");
        exit(0);
    }

    ft = fopen("temp.dat", "wb");
    if (ft == NULL)
    {
        printf("Cannot open file");
        fclose(fp);
        exit(0);
    }

    printf("Enter account number: ");
    scanf("%d", &accno);

    while (fread(&b, sizeof(b), 1, fp) == 1)
    {
        if (b.accno == accno)
        {
            printf("Name: %s", b.name);
            printf("Account number: %d", b.accno);
            printf("Balance: %d", b.balance);
            printf("Phone number: %s", b.phone);
            flag = 1;
        }
        else
            fwrite(&b, sizeof(b), 1, ft);
    }

    if (flag == 0)
        printf("Record not found");
    fclose(fp);
    fclose(ft);
    remove("bank.dat");
    rename("temp.dat", "bank.dat");
}

void main()
{
    int ch;
    while(1)
    {
        printf(" 1. Add new account\n 2. Balance enquiry \n 3. Close an account \n 4. Exit \n");
        printf("Enter your choice: ");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1: addA();
                break;
            case 2: balanceA();
                break;
            case 3: closeACC();
                break;
            case 4: exit(0);
            default: printf("Invalid choice");
        }
    getch();
    }
}