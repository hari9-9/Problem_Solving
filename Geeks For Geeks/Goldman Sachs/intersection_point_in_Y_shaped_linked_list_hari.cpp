/* Linked List Node
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}; */

/* Should return data of intersection point of two linked
   lists head1 and head2.
   If there is no intersecting point, then return -1. */
#include <bits/stdc++.h> 
int intersectPoint(Node* head1, Node* head2)
{
// Your Code Here
unordered_set<Node*>s;
while(head1)
{
s.insert(head1);
head1=head1->next;
}
while(head2)
{
if(s.find(head2)!=s.end())
{
return head2->data;
}
head2=head2->next;
}
return -1;
}
