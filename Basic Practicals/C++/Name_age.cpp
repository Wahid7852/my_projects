//stdlib to clear the screen
#include<stdlib.h>

#include<conio.h>
#include<iostream>

using namespace std;

class Person {
    int age;
    char name[30];

/* without the public keyword, 
 * the compiler treats the functions
 * as inside a private class
 */
 
    public:
    void getdata(void);
    void display(void);
};

void Person::getdata(void)
{
 cout<<"Enter name and age: "<<endl;
 cin>>name>>age;
}

void Person::display(void)
{
 cout<<"\n Your name is "<<name<<endl<<"\n Your age is "<<age<<endl;
}

int main()
{
 system("cls");
 Person p;
 p.getdata();
 p.display();
 getch();
return 0;
}