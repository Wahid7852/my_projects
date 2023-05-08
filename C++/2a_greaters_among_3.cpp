#include<conio.h>
#include<iostream>

using namespace std;

int main() {
    float a,b,c;
    system("cls");
    cout << "Enter 3 numbers: " << endl;
    cin >> a >> b >> c;

    if (a==0 || b==0 || c==0) {
        cout << "Please enter non zero values." << endl;
    } else if (a>b && a>c) {
        cout << a << " is the greatest number." << endl;
    } else if (b>a && b>c) {
        cout << b << " is the greatest number." << endl;
    } else if (c>a && c>b) {
        cout << c << " is the greatest number." << endl;
    } else if (a=b && c>a) {
        cout << c << " is the greatest number." << endl;    
    } else if (b=c && a>b) {
        cout << a << " is the greatest number." << endl;
    } else if (c=a && b>c) {
        cout << b << " is the greatest number." << endl;
    } else if (a=b && a>b) {
        cout << a << " and " << b << " are equal and greatest." << endl;
    } else if (b=c && b>a) {
        cout << b << " and " << c << " are equal and greatest." << endl;
    } else if (c=a && c>b) {
        cout << c << " and " << a << " are equal and greatest." << endl;
    } else if (a==b && a==c && b==c) {
        cout << "All three numbers are equal." << endl;
    }
    
    return 0;
}