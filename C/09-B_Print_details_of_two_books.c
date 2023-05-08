//program to print structure using title author subject and book id, print details of two students

#include<stdio.h>
#include<conio.h>

struct book
{
    char title[20];
    char author[20];
    char subject[20];
    int book_id;
};

void main()
{
    struct book book1, book2;
    printf("Enter details of book1: \n");
    printf("Enter title: ");
    gets(book1.title);
    printf("Enter author: ");
    gets(book1.author);
    printf("Enter subject: ");
    gets(book1.subject);
    printf("Enter book_id: \n\n");
    scanf("%d", &book1.book_id);

    printf("Enter details of book2: \n");
    printf("Enter title: ");
    gets(book2.title);
    printf("Enter author: ");
    gets(book2.author);
    printf("Enter subject: ");
    gets(book2.subject);
    printf("Enter book_id: \n\n");
    scanf("%d", &book2.book_id);

    printf("Displaying details of book1:  \n");
    printf("Title: %s \n", book1.title);
    printf("Author: %s \n", book1.author);
    printf("Subject: %s \n", book1.subject);
    printf("Book_id: %d \n\n", book1.book_id);
    printf("Displaying details of book2:  \n");
    printf("Title: %s \n", book2.title);
    printf("Author: %s \n", book2.author);
    printf("Subject: %s \n", book2.subject);
    printf("Book_id: %d \n", book2.book_id);
    getch();
}
