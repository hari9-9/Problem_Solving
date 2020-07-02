/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode *po = dummy;
        ListNode *p1 = dummy;
        //ListNode *po =new ListNode(head->val , head->next);
        //ListNode *p1 =new ListNode(head->val , head->next); 
        for(int i=1;i<=n+1;i++)
        {
            // p1->val = p1->next->val;
            p1 = p1->next;
        }
        while(p1!= NULL)
        {
            p1=p1->next;
            po=po->next;
        }
        po->next=po->next->next;

        
      return dummy->next;  
    }
};
