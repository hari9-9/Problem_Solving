class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head==NULL) return false;
        ListNode * temp2=head;
        int count=1;
        for(ListNode * temp = head->next; temp!=NULL; temp=temp->next)
        {
            if(count%2==0) temp2=temp2->next;
            if(temp==temp2) return true;
            count++;
        }
        return false;
    }
};
