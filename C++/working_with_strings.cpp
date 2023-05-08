//relational operators with string

#include <conio.h>
#include <string.h>
#include <iostream>
using namespace std;

void main() {
    string str1("hello");
    string str2("world");
    string str3 = str1+str2;
    
    if (str1 > str2) {
        cout << str1 << "is greater than " << str2;
    } else {
        cout << str2 << "is greater than " << str1; 
    }

    if (str1 != str2) {
        cout << str1 << "is not equal to " << str2;
    }

    if (str3 == str1 + str2) {
        cout << str1 << "is  equal to " << str2;
    }

    int s = str1.compare(str2);
    if (s==0) {
    cout << str1 << "=" << str2;
    } else if (s > 0) {
    cout << str1 << ">" << str2;
    } else {
        cout << str1 << "<" << str2;
    } 

    getch();
}