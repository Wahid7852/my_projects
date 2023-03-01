//4f multiple

#include <conio.h>
#include <iostream>
using namespace std;

class base1{
    public:
    int a1,a2;
    void getDatax() {
        cout<<"enter marks of eng and hindi = ";
        cin>>a1>>a2;
    }
};

class base2{
    public:
    int a3,a4,a5;
    void getDatay() {
        cout<<"enter marks of sci, hist and marathi = ";
        cin>>a3>>a4>>a5;
        }
};

class derive:public base1,public base2{    
    public:
    float avg;
    void product() {
        avg=a1+a2+a3+a4+a5/5;
        cout<<"Avg = "<<avg;
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