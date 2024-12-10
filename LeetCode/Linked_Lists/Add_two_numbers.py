# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,None)
        head = dummy
        carry =0
        while l1 and l2:
            ans = l1.val +l2.val+carry
            if ans > 9:
                ans = ans%10
                carry = 1
                node = ListNode(ans,None)
                dummy.next = node
                dummy = dummy.next
            else:
                carry = 0
                node = ListNode(ans,None)
                dummy.next = node
                dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            ans = l1.val+carry
            if ans > 9:
                ans = ans%10
                carry = 1
                node = ListNode(ans,None)
                dummy.next = node
                dummy = dummy.next
            else:
                carry = 0
                node = ListNode(ans,None)
                dummy.next = node
                dummy = dummy.next
            l1 = l1.next
        while l2:
            ans = l2.val+carry
            if ans > 9:
                ans = ans%10
                carry = 1
                node = ListNode(ans,None)
                dummy.next = node
                dummy = dummy.next
            else:
                carry = 0
                node = ListNode(ans,None)
                dummy.next = node
                dummy = dummy.next
            l2 = l2.next
        if carry:
            node = ListNode(carry,None)
            dummy.next = node
            dummy = dummy.next
        return head.next
