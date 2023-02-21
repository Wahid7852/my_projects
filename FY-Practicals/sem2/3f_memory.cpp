#include <conio.h>
#include <iostream>
using namespace std;

class Memory {
    const char*p;
    public:
    Memory() {
        p=new char[6];
        p="sweet";
    }

    void display() {
        cout<<p;
    }
};

int main() {
    Memory obj;
    system("cls");
    obj.display();
    getch();
    return 0;
}