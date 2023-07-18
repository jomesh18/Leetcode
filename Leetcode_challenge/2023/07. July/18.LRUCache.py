class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        self.curr_cap = 0

    def get(self, key: int) -> int:
        if key in self.d:
            val = self.remove(key)
            self.create_and_add_to_back(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(key)
        else:
            if self.curr_cap < self.capacity:
                self.curr_cap += 1
            else:
                to_delete = self.head.next.key
                self.remove(to_delete)
        self.create_and_add_to_back(key, value)

                
    def remove(self, key):
        node = self.d[key]
        val = node.val
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None
        del self.d[key]
        return val
        
    def create_and_add_to_back(self, key, val):
        node = Node(key, val)
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node
        self.d[key] = node
        return node
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
