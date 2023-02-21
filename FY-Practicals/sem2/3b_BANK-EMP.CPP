#include<conio.h>
#include<iostream>
using namespace std;

class Bank{
struct Emp
{
    char name[20];
    int acc_no;
    float bal;
}Em;

    public:
      void getData();
      void dispData();
};

void Bank::getData() {
    cout << "enter account holder name: " << endl;
    cin >> Em.name;
    cout << "enter account number: " << endl;
    cin >> Em.acc_no;
    cout << "enter balance amount: " << endl;
    cin >> Em.bal;
}

void Bank::dispData() {
    cout << endl << "Account details: " << endl << Em.name << endl << Em.acc_no << endl << Em.bal << endl;
}

int main() {
    Bank b;
    system("cls");
    b.getData();
    b.dispData();
    getch();
    return 0;
}