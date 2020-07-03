/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;
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
};
