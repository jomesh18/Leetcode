'''
1679. Max Number of K-Sum Pairs
Medium

1068

30

Add to List

Share
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
Accepted
68,575
Submissions
122,001
Seen this question in a real interview before?

Yes

No
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        c = 0
        for i, n in enumerate(nums):
            # print(d)
            if n in d:
                c += 1
                d[n].pop()
                if not d[n]: del d[n]
            else:
                d[k-n].append(i)
        return c

class Solution(object):
    def maxOperations(self, nums, k):
        ans = 0
        seen = defaultdict(int)
        for b in nums:
            a = k - b # Explain: a + b = k  =>  a = k - b
            if seen[a] > 0:
                ans += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return ans
        
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        c = 0
        for n in d:
            c += min(d[n], d[k-n])
        return c//2