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
        //ListNode * dummy = new ListNode(-1);
        //ListNode *head = dummy;
    ListNode* merger(ListNode* l1, ListNode* l2,ListNode * dummy)
    {
        if(l1 !=NULL && l2!=NULL)
        {
            if(l1->val < l2->val)
            {
                dummy->next = l1;
                //l1=l1->next
                return merger(l1->next, l2, dummy->next);
            }
            else
            {
                dummy->next = l2;
                //l2 = l2->next;
                return merger(l1, l2->next, dummy->next);
                
            }
            //dummy=dummy->next;
        }
        if(l1!=NULL)
            {
                dummy->next=l1;
                return dummy;
            }
            else
            {
            dummy->next=l2;
            return dummy;
            }

    }
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode * dummy = new ListNode(-1);
        ListNode *head = dummy;
        merger(l1,l2,dummy);
        return (head->next);
        
    }
};
