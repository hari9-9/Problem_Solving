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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode();
        ListNode *ref =head;
        int carry=0;
        int sum;
        while(l1 && l2)
        {
            sum=l1->val +l2->val+carry;
            if(sum>9)
            {
                sum=sum%10;
                carry=1;
                ListNode* node = new ListNode(sum);
                head->next =node;
                head=head->next;
                
            }
            else
            {
                carry=0;
                ListNode* node = new ListNode(sum);
                head->next =node;
                head=head->next;
            }
            l1=l1->next;
            l2=l2->next;
        }
        while(l1)
        {
            sum=l1->val + carry;
            if(sum>9)
            {
                sum=sum%10;
                carry=1;
                ListNode* node = new ListNode(sum);
                head->next =node;
                head=head->next;
                
            }
            else
            {
                carry=0;
                ListNode* node = new ListNode(sum);
                head->next =node;
                head=head->next;
            }
            l1=l1->next;
        }
        while(l2)
        {
            sum=l2->val+carry;
            if(sum>9)
            {
                sum=sum%10;
                carry=1;
                ListNode* node = new ListNode(sum);
                head->next =node;
                head=head->next;
                
            }
            else
            {
                carry=0;
                ListNode* node = new ListNode(sum);
                head->next =node;
                head=head->next;
            }
            l2=l2->next;
        }
        if(carry!=0)
        {
            ListNode* node = new ListNode(carry);
            head->next =node;
            head=head->next;
        }
        return ref->next;
        
    }
};
