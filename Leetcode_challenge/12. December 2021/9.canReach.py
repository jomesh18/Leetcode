'''
1306. Jump Game III
Medium

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

 

Constraints:

    1 <= arr.length <= 5 * 104
    0 <= arr[i] < arr.length
    0 <= start < arr.length

Accepted
109,035
Submissions
174,809
'''
# O(n) time, O(n) space
class Solution:
    def canReach(self, arr: [int], start: int) -> bool:
        self.visited = set()
        def helper(i):
            if i >= len(arr) or i < 0: return False
            if i in self.visited: return False
            self.visited.add(i)
            if arr[i] == 0:
                return True
            return helper(i+arr[i]) or helper(i-arr[i])
        return helper(start)

# O(n) time, O(1) space(not counting recursive stack) dfs
class Solution:
    def canReach(self, arr: [int], start: int) -> bool:
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False
        arr[start] *= -1
        return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])

# O(n) time, O(n) space, bfs
from collections import deque
class Solution:
    def canReach(self, arr: [int], start: int) -> bool:
        q = deque([start])
        while q:
            cur = q.popleft()
            if arr[curr] == 0: return True
            if arr[curr] < 0: continue
            if curr + arr[curr] < len(arr):
                q.append(curr+arr[curr])
            if curr - arr[curr] >= 0:
                q.append(curr-arr[curr])
            arr[curr] *= -1
        return False

arr = [4,2,3,0,3,1,2]
start = 5
# Output: true

# arr = [4,2,3,0,3,1,2]
# start = 0
# # Output: true 

# arr = [3,0,2,1,2]
# start = 2
# Output: false

sol = Solution()
print(sol.canReach(arr, start))
