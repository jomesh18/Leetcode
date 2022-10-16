'''
Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

#random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for num in nums if num == candidate) > majority_count:
                return candidate

#divide and conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi):
            #base case: only element in the array is the majority element
            if lo == hi:
                return nums[lo]
            
            #recurse on the left and right halves of this slice
            mid = (lo+hi)//2
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)
            
            # if two halves agree on the majority element
            if left == right:
                return left
            
            # otherwise, count each element and return the winner
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)
            
            return left if left_count  > right_count else right
        return majority_element_rec(0, len(nums)-1)

# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

# bit manipulation
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_element = 0
        bit = 1
        for i in range(31):
            # Count how many numbers have the current bit set.
            bit_count = sum(bool(num & bit) for num in nums)
            
            # If this bit is present in more than n / 2 elements
            # then it must be set in the majority element.
            if bit_count > n//2:
                majority_element += bit
                
            # Shift bit to the left one space. i.e. '00100' << 1 = '01000'
            bit <<= 1
            
        # In python 1 << 31 will automatically be considered as positive value
        # so we will count how many numbers are negative to determine if
        # the majority element is negative.
        is_neg = sum(num<0 for num in nums) > n//2
        
        # When evaluating a 32-bit signed integer, the values of the 1st through 
        # 31st bits are added to the total while the value of the 32nd bit is 
        # subtracted from the total. This is because the 32nd bit is responsible 
        # for signifying if the number is positive or negative.
        if is_neg:
            majority_element -= bit
            
        return majority_element