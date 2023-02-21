#include <conio.h>
#include <iostream>
using namespace std;

class Student {
    public:
    int roll_no;
    void print() {
        cout<<"roll no"<<roll_no;
    }
};

void main() {
    Student s, *sp;
    sp=&s;
    int Student::*ptr = &Student::roll_no;
    s.*ptr=10;
    s.print();
    sp->*ptr=20;
    sp->print();
    getch();
}