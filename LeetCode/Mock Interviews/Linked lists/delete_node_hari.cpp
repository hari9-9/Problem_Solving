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
    void deleteNode(ListNode* node) {
        ListNode* slow=node;
        ListNode* fast=node->next;
        while(fast->next!=NULL)
        {
            slow->val=fast->val;
            slow=slow->next;
            fast=fast->next;
        }
        slow->val=fast->val;
        slow->next=NULL;
        
    }
};
