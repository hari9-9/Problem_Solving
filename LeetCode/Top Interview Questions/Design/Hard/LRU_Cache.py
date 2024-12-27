class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # dummy to store recently used
        self.right = Node(0,0)
        #dummy to store LRU
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev= node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def addRecent(self,node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:

        if key in self.cache:
            ans = self.cache[key]
            self.remove(ans)
            self.addRecent(ans)
            return ans.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.addRecent(self.cache[key])

        if len(self.cache)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
