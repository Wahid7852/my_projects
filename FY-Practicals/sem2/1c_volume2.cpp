//P1 write program to calculate volume of square, sphere, rectangle
//P2 write program to convert seconds into hours, minutes and seconds

#include<stdlib.h>
#include<conio.h>
#include<iostream>

int main()
{
    float r, side, l, b, h, volsp, volsq, volrc, pi=3.14, choice;
    int s;
    system("cls");

    std::cout << " 1. Volume of Sphere \n 2. Volume of Square \n 3. Volume of rectangle \n" << std::endl << std::endl;
    std::cin >> s;
    switch(s) {
        case 1: 
        goto sp;
sp:
    std::cout <<"For volume of sphere \n Enter the radius: ";
    std::cin >> r;
    volsp=(4*pi*r*r*r)/3;
    std::cout << "Volume of the sphere is: "<< volsp << std::endl << std::endl;
        break;

        case 2:
        goto sq;
sq:
    std::cout <<"For volume of square \n Enter the side: ";
    std::cin >> side;
    volsq=side*side*side;
    std::cout << "Volume of the square is: "<< volsq << std::endl << std::endl;
        break;

        case 3:
        goto rc;
rc: 
    std::cout <<"For volume of rectangle \n Enter the length, breadth and height: ";
    std::cin >> l >> b >> h;
    volrc=l*b*h;
    std::cout << "Volume of the rectangle is: "<< volrc << std::endl << std::endl;
        break;

        default:
        std::cout << "Wrong choice!" << std::endl;
    }

return 0;

}