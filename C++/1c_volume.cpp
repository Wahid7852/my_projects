//P1 write program to calculate volume of square, sphere, rectangle
//P2 write program to convert seconds into hours, minutes and seconds

#include<stdlib.h>
#include<conio.h>
#include<iostream>

class Dec
{
    float r, secs, mins, hours, side, l, b, h, volsp, volsq, volrc, pi=3.14, choice;

    public:
    void sphere(void);
    void square(void);
    void rect(void);
};

void Dec::sphere() {
    std::cout <<"For volume of sphere \n Enter the radius";
    std::cin >> r;
    volsp=(4*pi*r*r*r)/3;
    std::cout << "Volume of the sphere is: "<< volsp << std::endl << std::endl;
}

void Dec::square() {
    std::cout <<"For volume of square \n Enter the side ";
    std::cin >> side;
    volsq=side*side*side;
    std::cout << "Volume of the square is: "<< volsq << std::endl << std::endl;
}

void Dec::rect() {
    std::cout <<"For volume of rectangle \n Enter the length, breadth and height";
    std::cin >> l >> b >> h;
    volrc=l*b*h;
    std::cout << "Volume of the rectangle is: "<< volrc << std::endl << std::endl;
}

int main()
{
    system("cls");
    Dec d;

d.square();
d.sphere();
d.rect();
return 0;
}
