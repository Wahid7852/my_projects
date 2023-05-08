#include <conio.h>
#include <iostream>
using namespace std;

class base{
    public:
    int x;
    void getData() {
        cout<<"enter value of x = ";
        cin>>x;
    }
};

class derive:public base{
    private:
    int y;
    
    public:
    void readData() {
        cout<<"Enter y: ";
        cin>>y;
    }

    void product() {
        cout<<"product = "<<x*y;
    }
};

int main() {
    derive a;
    a.getData();
    a.readData();
    a.product();
    return 0;
    getch();
}