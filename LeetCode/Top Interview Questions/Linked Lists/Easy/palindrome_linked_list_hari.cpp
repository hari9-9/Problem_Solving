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
    bool isPalindrome(ListNode* head) {
        ListNode * stack_build = head;
        stack <int> ele;
        while (stack_build!=NULL)
        {
            ele.push(stack_build->val);
            stack_build=stack_build->next;
        }
         int k=0;
        while(head !=NULL)
        {
            k=ele.top();
            ele.pop();
            if(k != head->val )
            {
                  return false;              
            }
            
            head= head->next;
        }
        
        return true;
    }
};
