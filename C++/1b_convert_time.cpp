//P1 write program to calculate volume of square, sphere, rectangle
//P2 write program to convert seconds into hours, minutes and seconds

#include<stdlib.h>
#include<conio.h>
#include<iostream>
using namespace std;

class Dec
{
    int total, secs, mins, hours;

    public:
    void convert(void);
};

void Dec::convert() {
    cout << "Enter total number of time"
    cin >> total;
    mins = total/60;
    secs = total % 60;
    hours = mins/60;
    mins = mins % 60;
    cout << total << " seconds is equivalent to " << hours << " hours " << mins << " minutes " << secs << " seconds.\n" ;
    }

int main()
{
    system("cls");
    Dec d;
    d.convert();
return 0;
}
