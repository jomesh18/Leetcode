'''
645. Set Mismatch
Easy

4316

1037

Add to List

Share
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_arr = [0]*n
        ans = []
        for num in nums:
            if num_arr[num-1]:
                ans.append(num)
            else:
                num_arr[num-1] += 1
        for i in range(n):
            if not num_arr[i]:
                ans.append(i+1)
        return ans


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        xor = 0
        for i, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
            xor ^= (i+1)^(abs(num))
        ans.append(ans[0]^xor)
        return ans