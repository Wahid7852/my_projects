//define a function to add 3 integers and return the sum.

#include<conio.h>
#include<iostream>

using namespace std; 

//function declaration
float avg(int, int, int);

int main() {
    int a=10, b=20, c=15;
    float f;
    system("cls");
//function call
    f=avg(a,b,c);
    cout << "average = " << f;
    return 0; 
}

//function definition
/*
 * If we use void instead of float, then the value wont be returned to f,
 * so the main function will not get the avg value, so we dont need to put 'f=' 
 * when we use void
 */
float avg(int p, int q, int r) {
    float v;
    v = (p+q+r)/3.0;
    return v;
}