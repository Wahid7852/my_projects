#include <conio.h>
#include <iostream>
using namespace std;

class Demo {    
        private:
        int num1,num2;

        public:
        Demo(int n1, int n2){ 
            num1=n1;
            num2=n2;
        }

        Demo(const Demo &n){
            num1=n.num1;
            num2=n.num2;
        }
        
        void display(){
            cout<<"num1 is : "<<num1<<endl;
            cout<<"num2 is : "<<num2<<endl;
            
        }
};

void main() {
    system("cls");
    Demo obj1(10, 20);
    Demo obj2 = obj1;
    obj1.display();
    obj2.display();
    getch();
}