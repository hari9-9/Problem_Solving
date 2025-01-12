class ListNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(-1) for _ in range(10**4)]  # Initialize dummy head nodes

    def add(self, key: int) -> None:
        index = key % len(self.set)
        curr = self.set[index]
        while curr.next:
            if curr.next.key == key:  # Check for duplicates
                return
            curr = curr.next
        curr.next = ListNode(key)  # Append new node

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        curr = self.set[index]
        while curr.next:
            if curr.next.key == key:  # Match found in curr.next
                curr.next = curr.next.next  # Remove the node
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        curr = self.set[index]
        while curr.next:
            if curr.next.key == key:  # Match found in curr.next
                return True
            curr = curr.next
        return False
