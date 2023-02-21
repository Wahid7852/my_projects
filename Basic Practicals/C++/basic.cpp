#include<conio.h>
#include<iostream>
using namespace std;

class Student {
    int a;
    char b[100];

    public:
        void get(void);
        void display(void);
};

void Student::get() {
    cout << "Enter student roll number" << endl;
    cin >> a;

    cout << "Enter student name" << endl << endl;
    cin >> b;
}

void Student::display() {
    cout << "Roll number of student is: " << a << endl;
    cout << "Name of student is: " << b << endl;
}

int main() {
    system("cls");
    Student s;
    s.get();
    s.display();
    //getch();
    return 0;
}