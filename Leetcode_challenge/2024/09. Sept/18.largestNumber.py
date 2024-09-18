'''
179. Largest Number
Medium

8355

699

Add to List

Share
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        def custom_sort(a, b):
            if len(a) != len(b):
                a, b = a + b, b+a
            for i in range(len(a)):
                if a[i] == b[i]:
                    continue
                elif a[i] > b[i]:
                    return True
                else:
                    return False
            return True
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a, b = nums[i], nums[j]
                if not custom_sort(a, b):
                    nums[i], nums[j] = b, a
            ans.append(nums[i])
            if all(i == '0' for i in ans):
                ans = ['0']
        return ''.join(ans)
                
