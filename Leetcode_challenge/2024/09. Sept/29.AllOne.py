'''
432. All O`one Data Structure
Hard

2045

200

Add to List

Share
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''
class Node:
    def __init__(self, f):
        self.f = f
        self.next = None
        self.prev = None
        self.keys = set()
    
    # def __str__(self):
    #     return 'f is '+str(self.f) + ' next is ' + str(self.next.f) + ' prev is '+str(self.prev.f) + ' keys are '+str(self.keys)
    
class AllOne:

    def __init__(self):
        self.d = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.d:
            if self.head.next.f != 1:
                node = Node(1)
                node.next = self.head.next
                self.head.next.prev = node
                self.head.next = node
                node.prev = self.head
                node.keys.add(key)
            else:
                self.head.next.keys.add(key)
            self.d[key] = self.head.next
        else:
            node = self.d[key]
            if not node.next or node.next.f != node.f + 1:
                new_node = Node(node.f+1)
                new_node.next = node.next
                new_node.prev = node
                node.next.prev = new_node
                node.next = new_node
            new_node = node.next
            new_node.keys.add(key)
            node.keys.remove(key)
            self.d[key] =  new_node
            if not node.keys:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None
            
    def dec(self, key: str) -> None:
        node = self.d[key]
        if node.f == 1:
            node.keys.remove(key)
            if not node.keys:
                self.head.next = node.next
                node.next.prev = self.head
                node.next = None
                node.prev = None
            del self.d[key]
        elif node.prev.f == node.f - 1:
            node.prev.keys.add(key)
            node.keys.remove(key)
            self.d[key] = node.prev
            if not node.keys:
                node.next.prev = node.prev
                node.prev.next = node.next
                node.next = None
                node.prev = None
        else:
            new_node = Node(node.f-1)
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node
            new_node.keys.add(key)
            self.d[key] = new_node
            node.keys.remove(key)
            
            if not node.keys:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None

    def getMaxKey(self) -> str:
        if self.tail.prev:
            for e in self.tail.prev.keys:
                return e
        return ''

    def getMinKey(self) -> str:
        if self.head.next:
            for e in self.head.next.keys:
                return e
        return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()