#include<iostream>
using namespace std;

int main() {

    int arr[10],i,num,n,c=0,pos;
    system("clear");
    cout << "Enter the array size : ";
    cin >> n;
    cout << "Enter the array elements : ";

    for(i=0;i<n;i++) {
        cin >> arr[i];
    }

    cout << "Enter the number to be searched : ";
    cin >> num;

    for (i=0; i<n; i++) {
        if(arr[i]==num) {
            c=1;
            pos=i+1;
            break;
        }
    }

    if(c==0) {
        cout << "Number not found..!!";
    } else {
        cout << num << " found at position " << pos;
    }

return 0;
}