class Solution {
public:
    
    ListNode * check(ListNode * head, ListNode * ptr)
    {
        if(ptr!=NULL)
        {
            head = check(head, ptr->next);
            if(head==NULL) return NULL;
            if(head==ptr || ptr->next==head)
            {
                head->val=-2147483648;
                return head;
            }
            if(head->val==-2147483648) return head;
        }
        else if(ptr==NULL) return head;
        if (head->val == ptr->val)
        {
            return head->next;
        }
        else return NULL;
    }
    
    bool isPalindrome(ListNode* head) {
        if(head==NULL) return true;
        ListNode * temp = check(head, head);
        if(temp==NULL) return false;
        else return true;
    }
};
