'''
Implement Stack using Queues

Solution
Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer. You can use more than two queues.
'''
# from collections import deque
# class MyStack:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.q1.append(x)

#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         if not self.empty():
#         	self.q2 = deque()
# 	        while len(self.q1) != 1:
# 	        	self.q2.append(self.q1.popleft())
# 	        ans = self.q1.popleft()
# 	        self.q1 = self.q2
# 	        return ans


#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         if not self.empty():
#         	self.q2 = deque()
# 	        while len(self.q1) != 1:
# 	        	self.q2.append(self.q1.popleft())
# 	        ans = self.q1.popleft()
# 	        self.q1 = self.q2
# 	        self.q1.append(ans)
# 	        return ans

#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not self.q1

#from leetcode, stefanpoch, one queue only

from collections import deque
class MyStack:

    def __init__(self):
        self._queue = deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)

# from leetcode, O(1) everything

class Stack(object):
    def __init__(self):
        self.queue = None

    def push(self, x):
        q = collections.deque()
        q.append(x)
        q.append(self.queue)
        self.queue = q

    def pop(self):
        self.queue.popleft()
        self.queue = self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

null = None
false = False
true = True

Input1 = ["MyStack", "push", "push", "top", "pop", "push", "empty"]
Input2 = [[], [1], [2], [], [], [3], []]
Output = [null, null, null, 2, 2, null, false]
out = [None]
obj = MyStack()

for fn, par in zip(Input1[1:], Input2[1:]):
	if fn == 'push':
		out.append(obj.push(par[0]))
	elif fn == 'pop':
		out.append(obj.pop())
	elif fn == 'top':
		out.append(obj.top())
	elif fn == 'empty':
		out.append(obj.empty())

print(Output)
print(out)

for u, v in zip(Output, out):
	if u != v:
		print(False)
		break
