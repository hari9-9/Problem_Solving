class Node:
    def __init__(self, key: str, value: str = None, next=None, prev=None):
        self.key = key
        self.value = value  # This can be used if you decide to store value in node as well.
        self.prev = prev 
        self.next = next

    def __repr__(self):
        return f"({self.key}:{self.value})"


class DLL:
    def __init__(self):
        self.head = Node("head")  # dummy head
        self.tail = Node("tail")  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_at_head(self, node: Node):
        """Insert a node right after the dummy head (marking it as most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self, node: Node):
        """Remove a node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_head(self, node: Node):
        """
        Move an existing node to the head (most recently used position).
        """
        self.remove_node(node)
        self.insert_at_head(node)
    
    def pop_tail(self):
        """
        Remove the node just before the dummy tail (the least recently used node)
        and return it.
        """
        if self.tail.prev == self.head:
            # List is empty
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node


class Storage:
    def __init__(self, capacity: int):
        self.store = {}      
        self.capacity = capacity
    
    def put(self, key: str, value: str):
        if key in self.store:
            self.store[key] = value  # update if exists
            return True
        if len(self.store) >= self.capacity:
            return False
        self.store[key] = value
        return True
    
    def get(self, key: str):
        return self.store.get(key, None)
    
    def remove(self, key: str):
        if key in self.store:
            del self.store[key]


class Eviction:
    def __init__(self):
        self.lru = DLL()
        self.mapper = {}  # maps key to node
    
    def update_access(self, key: str):
        if key in self.mapper:
            node = self.mapper[key]
            self.lru.move_to_head(node)
        else:
            node = Node(key)
            self.mapper[key] = node
            self.lru.insert_at_head(node)
            
    def evict(self):
        node = self.lru.pop_tail()
        if node:
            # Remove from our mapper
            evicted_key = node.key
            if evicted_key in self.mapper:
                del self.mapper[evicted_key]
            return evicted_key
        return None


class Cache:
    def __init__(self, capacity: int):
        self.capacity = capacity  
        self.storage = Storage(capacity)
        self.eviction = Eviction()
    
    def get(self, key: str):
        value = self.storage.get(key)
        if value is not None:
            # Only update recency if the key is present.
            self.eviction.update_access(key)
        return value
    
    def put(self, key: str, value: str):
        # If key already exists, update storage and refresh recency.
        if self.storage.get(key) is not None:
            self.storage.put(key, value)
            self.eviction.update_access(key)
            return
        
        # If storage.put returns False, the cache is full.
        if not self.storage.put(key, value):
            # Evict one item.
            evicted_key = self.eviction.evict()
            if evicted_key:
                self.storage.remove(evicted_key)
                print(f"Evicted key: {evicted_key}")
            # Try putting the new key now.
            self.storage.put(key, value)
        self.eviction.update_access(key)
    
    def __repr__(self):
        # For visualizing the keys in recency order
        node = self.eviction.lru.head.next
        keys = []
        while node != self.eviction.lru.tail:
            keys.append(node.key)
            node = node.next
        return " -> ".join(keys)


# Example usage:
if __name__ == "__main__":
    cache_capacity = 3
    cache = Cache(cache_capacity)
    
    cache.put("1", "one")
    cache.put("2", "two")
    cache.put("3", "three")
    print("Cache state:", cache)
    
    # Update recency on access
    print("Get key '2':", cache.get("2"))
    print("Cache state after accessing key 2:", cache)
    
    # Put a new key (should trigger eviction)
    cache.put("4", "four")
    print("Cache state after inserting key 4:", cache)
    
    # Try to get an evicted key
    print("Get key '1':", cache.get("1"))
