#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
};

class LinkedList
{
private:
    Node *head;

public:
    LinkedList()
    {
        head = nullptr;
    }

    void insert(int data)
    {
        Node *temp = new Node();
        temp->data = data;
        temp->next = nullptr;

        if (head == nullptr)
        {
            head = temp;
            return;
        }

        Node *temp1 = head;
        while (temp1->next != nullptr)
        {
            temp1 = temp1->next;
        }
        temp1->next = temp;
    }

    void display()
    {
        Node *temp = head;
        while (temp != nullptr)
        {
            cout << temp->data << "->";
            temp = temp->next;
        }
        cout << "nullptr" << endl;
    }

    void insertAtBeginning(int data)
    {
        Node *temp = new Node();
        temp->data = data;
        temp->next = head;
        head = temp;
    }

    void insertAtPosition(int data, int position)
    {
        if (position <= 0)
        {
            cout << "Invalid position" << endl;
            return;
        }

        Node *temp = new Node();
        temp->data = data;
        temp->next = nullptr;

        if (position == 1)
        {
            temp->next = head;
            head = temp;
            return;
        }

        Node *temp1 = head;
        for (int i = 0; i < position - 2 && temp1 != nullptr; i++)
        {
            temp1 = temp1->next;
        }

        if (temp1 == nullptr)
        {
            cout << "Invalid position" << endl;
            delete temp;
            return;
        }

        temp->next = temp1->next;
        temp1->next = temp;
    }

    void deleteNode(int position)
    {
        if (head == nullptr)
        {
            cout << "List is empty" << endl;
            return;
        }

        if (position <= 0)
        {
            cout << "Invalid position" << endl;
            return;
        }

        Node *temp = head;
        if (position == 1)
        {
            head = temp->next;
            delete temp;
            return;
        }

        for (int i = 0; i < position - 2 && temp != nullptr; i++)
        {
            temp = temp->next;
        }

        if (temp == nullptr || temp->next == nullptr)
        {
            cout << "Invalid position" << endl;
            return;
        }

        Node *temp1 = temp->next;
        temp->next = temp1->next;
        delete temp1;
    }

    void searchAndDisplay(int target)
    {
        Node *current = head;
        while (current)
        {
            if (current->data == target)
            {
                cout << "Found " << target << endl;
                return;
            }
            current = current->next;
        }
        cout << "Not found " << target << endl;
    }

    ~LinkedList()
    {
        Node *temp = head;
        while (temp != nullptr)
        {
            Node *next = temp->next;
            delete temp;
            temp = next;
        }
    }
};

int main()
{
    LinkedList list;

    cout << "Create a linked list:" << endl;
    int n, data;
    cout << "Enter the number of elements: ";
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout << "Enter element " << i + 1 << ": ";
        cin >> data;
        list.insert(data);
    }

    int choice;
    while (true)
    {
        cout << endl << "1. Display the list" << endl;
        cout << "2. Insert a node at the beginning" << endl;
        cout << "3. Insert a node at a given position" << endl;
        cout << "4. Delete a node" << endl;
        cout << "5. Search for a node" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        cout << endl;

        switch (choice)
        {
        case 1:
            list.display();
            cout << endl;
            break;
        case 2:
            cout << "Enter data: ";
            cin >> data;
            list.insertAtBeginning(data);
            list.display();
            cout << endl;
            break;
        case 3:
            cout << "Enter data: ";
            cin >> data;
            int position;
            cout << "Enter position: ";
            cin >> position;
            list.insertAtPosition(data, position);
            list.display();
            cout << endl;
            break;
        case 4:
            cout << "Enter position: ";
            cin >> position;
            list.deleteNode(position);
            list.display();
            cout << endl;
            break;
        case 5:
            cout << "Enter the target: ";
            cin >> data;
            list.searchAndDisplay(data);
            cout << endl;
            break;
        case 6:
            exit(0);
        default:
            cout << "Invalid choice" << endl;
        }
    }

    return 0;
}
