/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
    Node *slow = head;
    Node *fast = head;
        bool flag =false;
        int i=1;
        
        while(fast!= NULL && flag==false)
        {
            fast=fast->next;
            if(i%2==0)
            {
                slow=slow->next;
            }
            i++;
            if(fast==slow)
            {
                flag=true;
                
            }
            
        }
        if(flag==true)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    
}
