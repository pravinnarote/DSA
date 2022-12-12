/*
linked list madeup of collection of nodes.
single node shows an data and contains adress of next node.
        ....................
        :   data :  next    :
        ....................
this is dynamic data stuture.no memory wastage.
delection is easy.no shift needed.
types:
1)singly linked list.
2)double linked list
3)circular linked list
-----******single node shows an data and contains adress of next node.-----******
*/
#include <iostream>
using namespace std;
struct node
{
        int data;
        struct node *next;
};
int main()
{
        struct node *head = NULL;
        head = (struct node *)malloc(sizeof(struct node));
        head->data = 45;
        head->next = NULL;
        cout << head->data;
        return 0;
}
