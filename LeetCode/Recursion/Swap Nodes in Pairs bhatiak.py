# Hari's solution.

class Solution:
    
    def swaps(self, p1, p2, p3):
        
        if p2 and p3:
            temp = p3.next
            p1.next=p3
            p3.next=p2
            p2.next = temp
            
            if p2 and p2.next:
                self.swaps(p2, p2.next, p2.next.next)
    
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        dummy = ListNode(-1, head)
        
        self.swaps(dummy, head, head.next)
        return dummy.next
