class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count=0;
        ListNode *p1=head, *p2=head;
        for(; p1!=NULL; p1=p1->next)
        {
            count++;
            if(count>(n+1)) p2=p2->next;
        }

        if (count==n) {
            return head->next;
        }
        p2->next=p2->next->next;
        
        return head;
    }
};
