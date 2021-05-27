'''
Min Stack

Solution
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()[0]        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return float('inf')

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
null = None
inp = ["MinStack","push","push","push","getMin","pop","top","getMin"]
para = [[],[-2],[0],[-3],[],[],[],[]]
out = [null,null,null,null,-3,null,0,-2]
obj = MinStack()
print(obj.stack)
ans = [None]
for fun, par in zip(inp[1:], para[1:]):
    if fun == "push":
        ans.append(obj.push(par[0]))
    if fun == "pop":
        ans.append(obj.pop())
    if fun == "top":
        ans.append(obj.top())
    if fun == "getMin":
        ans.append(obj.getMin())
    print(obj.stack)

print(ans)