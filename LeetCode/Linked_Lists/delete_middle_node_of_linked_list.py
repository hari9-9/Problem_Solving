# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        if not head.next:
            return None
        slow = dummy_node
        fast = head
        i=0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_node.next
        
