'''
Open the Lock

Solution
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
'''
'''
   Hide Hint #1  
We can think of this problem as a shortest path problem on a graph: there are `10000` nodes (strings `'0000'` to `'9999'`), and there is an edge between two nodes if they differ in one digit, that digit differs by 1 (wrapping around, so `'0'` and `'9'` differ by 1), and if *both* nodes are not in `deadends`.
'''

#my try, bfs
# from collections import deque
# class Solution:
#     def openLock(self, deadends: [str], target: str) -> int:
#         if '0000' in deadends: return -1
#         if target == '0000': return 0
#         q = deque(['0000'])
#         step = 0
#         visited = set()
#         while q:
#             step += 1
#             l = len(q)
#             for _ in range(l):
#                 c = q.popleft()
#                 for i in range(len(c)):
#                     n1 = c[:i]+str((int(c[i])-1)%10)+c[i+1:]
#                     n2 = c[:i]+str((int(c[i])+1)%10)+c[i+1:]
#                     to_add = [n for n in [n1, n2] if n not in visited and n not in deadends]
#                     if target in to_add: return step
#                     visited.update(to_add)
#                     q.extend(to_add)
#         return -1

# my try bfs, modified
from collections import deque
class Solution:
    def openLock(self, deadends: [str], target: str) -> int:
        visited, q, step = set(deadends), deque(['0000']), -1
        while q:
            step += 1
            l = len(q)
            for _ in range(l):
                c = q.popleft()
                if c not in visited:
                    visited.add(c)
                    if c == target: return step
                    for i in range(len(c)):
                        n1 = c[:i]+str((int(c[i])-1)%10)+c[i+1:]
                        n2 = c[:i]+str((int(c[i])+1)%10)+c[i+1:]
                        q.extend([n1, n2])
        return -1

# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
# Output: 6
# deadends = ["8888"]
# target = "0009"
# Output: 1
# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
# # Output: -1
# deadends = ["0000"]
# target = "8888"
# Output: -1
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0000"
# Output: 0
s = Solution()
print(s.openLock(deadends, target))
