'''
3721. Longest Balanced Subarray II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.

 

Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
Example 3:

Input: nums = [1,2,3,2]

Output: 3

Explanation:

The longest balanced subarray is [2, 3, 2].
It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''
class SegmentTree:
    def __init__(self, n):
        self.max = [0]*(4*n)
        self.min = [0]*(4*n)
        self.lazy = [0]*(4*n)
        self.n = n

    def propogate(self, pos, l, r):
        if self.lazy[pos] != 0:
            self.max[pos] += self.lazy[pos]
            self.min[pos] += self.lazy[pos]
            if l != r:
                self.lazy[2*pos+1] += self.lazy[pos]
                self.lazy[2*pos+2] += self.lazy[pos]
            self.lazy[pos] = 0

    def query(self, start, end, val):
        return self.query_helper(start, end, 0, 0, 0, self.n-1)

    def query_helper(self, start, end, val, pos, l, r):
        self.propogate(pos, l, r)
        if self.max[pos] < val or self.min[pos] > val:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        left = self.query_helper(start, end, val, 2*pos+1, l, mid)
        if left != -1:
            return left
        return self.query_helper(start, end, val, 2*pos+2, mid+1, r)

    def update_range(self, start, end, val):
        return self.update_range_helper(start, end, val, 0, 0, self.n-1)

    def update_range_helper(self, start, end, val, pos, l, r):
        self.propogate(pos, l, r)
        if r < start or l > end:
            return
        if l >= start and r <= end:
            self.lazy[pos] += val
            self.propogate(pos, l, r)
            return 
        mid = (l + r) // 2
        self.update_range_helper(start, end, val, 2*pos+1, l, mid)
        self.update_range_helper(start, end, val, 2*pos+2, mid+1, r)
        self.min[pos] = min(self.min[2*pos+1], self.min[2*pos+2])
        self.max[pos] = max(self.max[2*pos+1], self.max[2*pos+2])

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        seen = {}
        ans = 0
        for i in range(n):
            val = -1 if nums[i] & 1 else 1
        
            prev_idx = -1
            if nums[i] in seen:
                prev_idx = seen[nums[i]]
            if prev_idx != -1:
                st.update_range(0, prev_idx, -val)

            st.update_range(0, i, val)

            idx = st.query(0, i, 0)
            if idx != -1:
                ans = max(ans, i - idx + 1)

            seen[nums[i]] = i

        return ans
