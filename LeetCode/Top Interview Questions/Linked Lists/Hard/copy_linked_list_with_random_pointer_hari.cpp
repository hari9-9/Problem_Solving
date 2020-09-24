/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* fast=head->next;
        Node* slow=head;
        while(fast)
        {
            Node* c=new Node(slow->val);
            c->next = slow->next;
            slow->next=c;
            fast=fast->next;
            slow=slow->next->next;
        }
        Node* c=new Node(slow->val);
        slow->next=c;
        // slow=head;
        // while(slow)
        // {
        //     slow->val=-1;
        //     slow=slow->next->next;
        // }
        // slow=head;
        // while(slow)
        // {
        //     cout<<slow->val<<endl;
        //     slow=slow->next;
        // }
        fast=head->next;
        Node * ans =fast;
        slow=head;
        while(fast)
        {
            
            if(slow->random)
                fast->random=slow->random->next;
            else
                fast->random=NULL;
            if(fast->next)
            {
                Node * temp = fast->next;
                cout<<&fast->val<<" "<<&slow->val<<" "<<temp->val<<endl;
                fast=fast->next->next;
                slow->next=temp;
                slow=slow->next;
                cout<<fast->val<<" "<<slow->val<<endl;
                
            }
            else
            {
                cout<<"Manual";
                fast->next=NULL;
                break;  
            }
            
        }
        slow->next=NULL;
        // slow=head;
        // while(slow)
        //  {
        //      slow->val=-1;
        //      slow=slow->next;
        //  }
        // slow=ans;
        // while(slow)
        // {
        //     if(slow->random)
        //         cout<<slow->val<<" "<<slow->random->val<<endl;
        //     else
        //         cout<<slow->val<<"NULL"<<endl;
        //     slow=slow->next;
        // }
        
        
        return ans;
        
        
    }
};
