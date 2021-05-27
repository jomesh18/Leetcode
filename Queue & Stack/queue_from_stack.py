'''
Implement Queue using Stacks

Solution
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
'''

# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.s1 = []
#         self.s2 = []

#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         self.s2.append(x)

#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         if not self.empty():
#             while self.s2:
#                 self.s1.append(self.s2.pop())
#             elem = self.s1.pop()
#             while self.s1:
#                 self.s2.append(self.s1.pop())
#             return elem
#         return None

#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         if not self.empty():
#             self.s1 = self.s2[:]
#             while len(self.s1) != 1:
#                 self.s1.pop()
#             return self.s1.pop()

#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         return len(self.s2) == 0
        

#from leetcode top

class MyQueue:

    def __init__(self):
        self._enq = []
        self._deq = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._enq.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
                
        return self._deq.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
                
        return self._deq[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._enq and not self._deq        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

null = None
false = False
true = True
Input1 = ["MyQueue", "push", "push", "peek", "pop", "empty"]
Input2 = [[], [1], [2], [], [], []]
Output = [null, null, null, 1, 1, false]

Input1 = ["MyQueue","empty"]
Input2 = [[],[]]
Output = [null,true]

out = [None]
obj = MyQueue()
for fn, para in zip(Input1[1:], Input2[1:]):
    if fn == 'push':
        out.append(obj.push(para[0]))
    elif fn == 'peek':
        out.append(obj.peek())
    elif fn == 'pop':
        out.append(obj.pop())
    elif fn == 'empty':
        out.append(obj.empty())

print(Output)
print(out)
for a1, a2 in zip(Output, out):
    if (a1 != a2):
        print(False)
        break
