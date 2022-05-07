'''
456. 132 Pattern
Medium

3699

202

Add to List

Share
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
Accepted
116,484
Submissions
374,696
Seen this question in a real interview before?

Yes

No
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        min_arr = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            min_arr[i] = min(min_arr[i-1], nums[i])
            
        stack = []
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > min_arr[j]:
                while stack and stack[-1] <= min_arr[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False

class Solution:
    def find132pattern(self, nums):
        stack = []
        s3 = float("-inf")
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False