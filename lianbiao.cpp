#include<iostream>
using namespace std;
class Node
{
public:
	int data;
	Node* next;
	Node(int data)
	{
		this->data = data;
		this->next = nullptr;
	}
};
class NodeList
{
public:
	Node* head=nullptr;
	Node* tail=nullptr;
	void Add(int data)
	{
		Node* newnode = new Node(data);
		if (head == nullptr)
		{
			head = newnode;
			tail = newnode;
			tail->next = head;
		}
		else
		{
			tail->next = newnode;
			tail = newnode;
			tail->next = head;
		}
	}
	void del(int data)
	{
		Node* curr = head;
		Node* prev = nullptr;
		if (curr->data == data)
		{
			head = head->next;
			tail->next = head;
			return;
		}
		curr = head->next;
		prev = head;
		while (curr != head)
		{
			if(curr->data==data&&curr!=tail)
			{
				prev->next = curr->next;
				return;
			}
			if (curr==tail && curr->data == data)
			{
				tail = prev;
				tail->next = head;
				return;
			}
			curr = curr->next;
			prev = prev->next;
		}
	}
    void dispaly()
    {
        Node* curr = head;
        while (curr->next != head)
        {
            cout << curr->data << " ";
            curr = curr->next;
        }
        cout << curr->data << endl;
    }
};
int main()
{
    NodeList n;
    n.Add(1);
    n.Add(2);
    n.Add(3);
    n.Add(4);
    n.Add(5);
    n.Add(6);
    n.Add(7);
    n.Add(8);
    n.Add(9);
    n.Add(10);
    n.dispaly();
    n.del(1);
    n.dispaly();
    n.del(10);
    n.dispaly();
    n.del(5);
    n.dispaly();
    return 0;
}