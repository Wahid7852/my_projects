#include <conio.h>
#include <iostream>
using namespace std;

class a;
class b{
    int number;
    public:
        b(int x) 
        {
            number=x;
        }
void friend greatest(a a1,b b1);
};

class a {
    int number;
    public:
    a(int x){
        number=x;
    }
void friend greatest(a a1,b b1);
};

void greatest(a a1, b b1) {
    if(a1.number > b1.number) {
        cout<<"larest number A is :"<<a1.number;
    } else if(a1.number < b1.number) {
        cout<<"larest number B is :"<<b1.number;
    } else {
        cout<<"both are equal";
    }
}

int main() {
    int num;
    cout<<"enter number 1: "<<endl;
    cin>>num;
    a a1(num);

    cout<<"enter number 2: "<<endl;
    cin>>num;
    b b1(num);
    
    greatest(a1,b1);
    cout<<"\n";
    getch();
    return 0;
}
