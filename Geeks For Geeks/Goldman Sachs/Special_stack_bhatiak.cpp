#include<iostream>
using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    struct Node {
        int val;
        Node * next, *nextMin;
        
        Node (int x) {
            this->val=x;
            this->next=NULL;
            this->nextMin=NULL;
        }
    };

    Node * Top, *minNode;
    MinStack() {
        Top = NULL;
    }
    
    void push(int x) {
        Node * temp = new Node(x);
        if (Top == NULL) {
            Top=temp;
            minNode=temp;
        }
        else {
            if (x < minNode->val) {
                temp->nextMin = minNode;
                minNode = temp;
            }
            temp->next=Top;
            Top=temp;
        }
    }
    
    void pop() {
        if (Top == minNode) {
            minNode = minNode->nextMin;
        }
        Top = Top->next;
    }
    
    int top() {
        return Top->val;
    }
    
    int getMin() {
        return minNode->val;
    }
};
