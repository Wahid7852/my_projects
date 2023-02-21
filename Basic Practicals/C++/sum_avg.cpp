#include <stdlib.h>
#include <conio.h>
#include <iostream>

int main()
{
    float a,b,sum,avg;
    //clear the screen
    system("cls");
    std::cout << "Enter the first number: " << std::endl;
    std::cin >> a;
    std::cout << "Enter the second number: " << std::endl;
    std::cin >> b;
    sum=a+b;
    avg=sum/2;

    std::cout << "The sum of the two numbers is: " << sum << std::endl;
    std::cout << "The average of the two numbers is: " << avg << std::endl;
    getch();
return 0;
}
