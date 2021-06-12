# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap=[]
        for list in lists:
            while list!=None:
                heap.append(list.val)
                list=list.next
        heapq.heapify(heap)
        p=ListNode();
        if not len(heap):
            return 
        head=ListNode(next=p)
        while(len(heap)!=1):
            p.val=heapq.heappop(heap)
            p.next=ListNode()
            p=p.next
        p.val=heapq.heappop(heap)
        return head.next
