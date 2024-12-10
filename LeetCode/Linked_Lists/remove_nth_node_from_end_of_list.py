# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move `fast` n+1 steps ahead to maintain a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both `fast` and `slow` until `fast` reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        # Return the head of the updated list
        return dummy.next
