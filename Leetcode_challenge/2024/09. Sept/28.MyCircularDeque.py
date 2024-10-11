'''
641. Design Circular Deque
Medium

1583

100

Add to List

Share
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
 

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
'''
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.front = None
        self.last = None
        self.l = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.front = Node(value)
            self.last = self.front
        else:
            curr = Node(val=value, next=self.front, prev=self.last)
            self.front.prev = curr
            self.front = curr
            self.last.next = curr
        self.l += 1
        return True
            
    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.last = Node(value)
            self.front = self.last
        else:
            curr = Node(val=value, next=self.front, prev=self.last)
            self.last.next = curr
            self.last = curr
            self.front.prev = curr 
        self.l += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        if self.l == 1:
            self.front = None
            self.last = None
        else:
            temp = self.front.next
            self.last.next = temp
            temp.prev = self.last
            self.front = temp
        self.l -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        if self.l == 1:
            self.front = None
            self.last = None
        else:
            temp = self.last.prev
            temp.next = self.front
            self.front.prev = temp
            self.last = temp
        self.l -= 1
        return True

    def getFront(self) -> int:
        return self.front.val if self.l else -1

    def getRear(self) -> int:
        return self.last.val if self.l else -1

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()