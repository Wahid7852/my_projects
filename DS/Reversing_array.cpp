#include<iostream>
using namespace std;

int main() {
    
    int arr[10],i,n;
    system("clear");
    cout << "Enter the array size : ";
    cin >> n;
    cout << "Enter the array elements : ";
    for (i=0; i<n; i++) {
        cin >> arr[i];
    }

    // normal
    cout << "\nPrinting the array elements: \n";
    for (i=0; i<n; i++) {
        cout << arr[i] << " ";
    }

    cout << "\narray elements in reverse: \n" << endl;
    for (i=n-1; i>=0; i--) {
        cout << arr[i] << " ";
    }

return 0;
}