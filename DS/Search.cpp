#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *next;
};

Node *head = NULL;

void insert(int data) {
    Node *temp = new Node();
    temp->data = data;
    temp->next = NULL;

    if (head == NULL) {
        head = temp;
        return;
    }

    Node *temp1 = head;
    while (temp1->next != NULL) {
        temp1 = temp1->next;
    }
    temp1->next = temp;
}

void searchAndDisplay(int target) {
    Node *current = head;
    while (current) {
        if (current->data == target) {
            cout << "Found " << target << endl;
            return;
        }
        current = current->next;
    }
    cout << "Not found " << target << endl;
}

void display() {
    Node *temp = head;
    while (temp != NULL) {
        cout << temp->data << "->";
        temp = temp->next;
    }
}

int main() {
    int n, data;
    cout << "Enter the number of nodes: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Enter data: ";
        cin >> data;
        insert(data);
    }

    cout << "Enter the target: ";
    cin >> data;
    searchAndDisplay(data);
    return 0;
}



