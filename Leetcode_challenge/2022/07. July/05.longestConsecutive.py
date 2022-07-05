'''
128. Longest Consecutive Sequence
Medium

11197

483

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
765,988
Submissions
1,564,479
'''
#O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = list(set(nums))
        nums.sort()
        l = 1
        max_l = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                l += 1
                max_l = max(max_l, l)
            else:
                l = 1
        return max_l

#O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        num_set = set(nums)
        for n in num_set:
            if n - 1 not in num_set:
                curr_n = n
                curr_streak = 1
                while curr_n + 1 in num_set:
                    curr_n += 1
                    curr_streak += 1
                max_streak = max(max_streak, curr_streak)
        return max_streak

#Union find
class UF:
    def __init__(self, l):
        self.root = [i for i in range(l)]
        self.rank = [0]*l
        self.size = [1]*l
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.root[py] = px
                self.size[px] += self.size[py]
            else:
                self.root[px] = py
                self.size[py] += self.size[px]
                if self.rank[px] == self.rank[py]:
                    self.rank[py] += 1
                    
    def is_connected(self, x, y):
        px, py = self.find(x), self.find(y)
        return px == py
    
    def get_max_connected_component(self):
        return max(self.size) if self.size else 0

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        uf = UF(len(nums))
        val_to_ind = {}
        for i, num in enumerate(nums):
            if num not in val_to_ind:
                val_to_ind[num] = i
                if num + 1 in val_to_ind:
                    uf.union(i, val_to_ind[num+1])
                if num - 1 in val_to_ind:
                    uf.union(i, val_to_ind[num-1])
                    
        return uf.get_max_connected_component()
