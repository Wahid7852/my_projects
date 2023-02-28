#include <conio.h>
#include <iostream>
using namespace std;

class Base{
    public:
    int x,y;
    
    void getDatax() {
        cout<<"Enter value of x = ";
        cin>>x;
    }
    
    void getDatay() {
        cout<<"Enter value of y: ";
        cin>>y;
    }

};

class Calc:public Base{    
    public:
    void product() {
        cout<<"\nProduct of x and y is = "<<x*y;
    }
};

class Base1:public Base{
    public:
    void ShowDataX() {
        cout<<"Memory value of X is = "<<&x;
    }
};

class Base2:public Base{
    public:
    void ShowDataY() {
        cout<<"\n Memory value of Y is = "<<&y;
    }
};

int main() {
    system("cls");
    Base1 a;
    Base2 b;
    Calc c;
    c.getDatax();
    c.getDatay();
    a.ShowDataX();
    b.ShowDataY();
    c.product();

    return 0;
    getch();
}