'''
895. Maximum Frequency Stack
Hard

2905

45

Add to List

Share
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
Accepted
102,337
Submissions
156,437
'''
from collections import Counter, defaultdict
# O(n)
# class FreqStack:

#     def __init__(self):
#         self.freq = Counter()
#         self.group = defaultdict(list)
#         self.maxfreq = 0

#     def push(self, val: int) -> None:
#         f = self.freq[val] + 1
#         self.freq[val] = f
#         self.group[f].append(val)
#         if f > self.maxfreq: self.maxfreq = f
        
#     def pop(self) -> int:
#         val = self.group[self.maxfreq].pop()
#         self.freq[val] -= 1
#         if not self.group[self.maxfreq]:
#             self.maxfreq -= 1
#         return val

#priority queue, O(nlogn)
import heapq
class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.st = []
        self.count = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        heapq.heappush(self.st, (-f, -self.count, val))
        self.freq[val] = f
        self.count += 1

    def pop(self) -> int:
        f, count, val = heapq.heappop(self.st)
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

st = FreqStack()
st.push(5)
st.push(7)
st.push(5)
st.push(7)
st.push(4)
st.push(5)
# print(st.freq, st.group)
# st.pop()
# print(st.freq, st.group)
# st.pop()
# print(st.freq, st.group)
# st.pop()
# print(st.freq, st.group)
# st.pop()
# print(st.freq, st.group)

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()