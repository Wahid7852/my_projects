//4f multiple

#include <conio.h>
#include <iostream>
using namespace std;

class base1{
    public:
    int x;
    void getDatax() {
        cout<<"enter value of x = ";
        cin>>x;
    }
};

class base2{
    public:
    int y;
    void getDatay() {
        cout<<"Enter value of y: ";
        cin>>y;
    }
};

class derive:public base1,public base2{    
    public:
    void product() {
        cout<<"product = "<<x*y;
    }
};

int main() {
    derive a;
    a.getDatax();
    a.getDatay();
    a.product();
    return 0;
    getch();
}