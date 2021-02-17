'''
Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

 

Constraints:

    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

 
Follow up: Could you solve the problem without using the built-in queue? 
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.l = [None] * k
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        k = len(self.l)
        if self.isEmpty():
            self.head = self.tail = 0
            self.l[self.tail] = value
            print(self.head, self.tail, self.l)
        elif self.isFull():
            return False
        elif self.tail < k-1:
            self.tail += 1
            self.l[self.tail] = value
            print(self.head, self.tail, self.l)
        elif self.tail == k-1:
            self.tail = 0
            self.l[self.tail] = value
        return True

    def deQueue(self) -> bool:
        k = len(self.l)
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = self.tail = None
            return False
        elif self.head<k-1:
            self.head += 1
            self.l[self.head] = value
        elif self.head == k-1:
            self.head = 0
            self.l[self.head] = value
        return True

    def Front(self) -> int:
        return self.l[self.head] if self.head is not None else -1

    def Rear(self) -> int:
        return self.l[self.tail] if self.tail is not None else -1

    def isEmpty(self) -> bool:
        a = True if self.head is not None else False
        print(a)
        return True if self.head is not None else False

    def isFull(self) -> bool:
        if self.head is not None:
            if (self.tail - self.head == k-1) or (self.head - self.tail == 1):
                return True
        return False

    def __str__(self):
        if self.head is not None:
            if self.head<=self.tail:
                return str(l[self.head:self.tail+1])
            else:
                return str(l[:self.tail+1]+l[self.head:])
        return 'None'


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]
q = MyCircularQueue(3)
# print(q)
# print(q.l)
# print(q.head)
# print(q.tail)
# i = 0
# for _ in range(4):
#     i+=1
#     print(q.enQueue(i))
# print(q)
print(q.enQueue(1))
# # print(q.enQueue(2))
# # print(q.enQueue(3))
# # print(q.enQueue(4))
# print(q.Rear())
# print(q.isFull())
# print(q.deQueue())
# print(q.Rear())
