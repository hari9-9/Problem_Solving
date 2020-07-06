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
    void swap_rec(ListNode* back ,ListNode* curr , ListNode*forward)
    {
        if(curr && forward)
        {
            ListNode * temp = forward->next;
            back->next = forward;
            forward->next = curr;
            curr->next = temp;
            back = curr;
            if(back && back->next)
            swap_rec(back , back->next , back->next->next);
        }
    }
    ListNode* swapPairs(ListNode* head) {
        //cout<<head->next->next->val;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        if(!head)
            return {};
        swap_rec(dummy,head,head->next);
        return dummy->next;
    }
};
