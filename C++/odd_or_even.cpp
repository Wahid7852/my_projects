#include<conio.h>
#include<iostream>
using namespace std;

int main()
{
	int n, a, eS=0, oS=0;
	system("cls");
	cout << "Enter a number=  " << endl;
	cin >> a;	
	
	for(n=1; n<=a; n++)
	{
  		if (n%2==0) 
		{
			eS=eS+n;
            system("cls");
        	cout << "Sum of Even numbers is: " << eS << endl << endl;
		}
		else if (n%2!=0) {
			oS=oS+n;
            system("cls");
         	cout << "Sum of Odd numbers is " << oS << endl << endl;
		}
	}


 	return 0;
}