class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode * new_list = NULL;
        for (ListNode * temp=head; temp!=NULL; temp=temp->next)
        {
            ListNode * t = new ListNode(temp->val);
            t->next=new_list;
            new_list=t;
        }
        return new_list;
    }
};
