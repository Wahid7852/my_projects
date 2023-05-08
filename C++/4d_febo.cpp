#include <conio.h>
#include <iostream>
using namespace std;

class febo {
    long int a,b;
    public:
    febo(){
        a=-1;
        b=1;
    }

    void febser(int n){
        int i, next;
        cout<<"\nResultant febo \n";
        for(i=0;i<n;i++) {
            next=a+b;
            cout<<" "<<next;
            a=b;
            b=next;
        }
    }
};

int main() {
    febo f;
    int n;
    system("cls");
    cout<<"Febo series: \n";
    cout<<"Enter range: ";
    cin>>n;
    f.febser(n);
    return 0;
    getch();
}
