'''
287. Find the Duplicate Number
Medium

13053

1474

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
Accepted
797,621
Submissions
1,357,886
'''
#sorting
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: return nums[i]

#using negative to mark
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n] < 0: return n
            nums[n] = -nums[n]
            
#i to nums[i], recursive
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def helper(i):
            if nums[i] == i:
                return i
            next_i = nums[i]
            nums[i] = i
            return helper(next_i)
        return helper(0)
    
#everything to nums[0], iterative
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        while nums[0] != nums[nums[0]]:
            nums[0], nums[nums[0]] = nums[nums[0]], nums[0]
        return nums[0]

#binary search O(nlogn)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def count_(n):
            c = 0
            for num in nums:
                if num <= n:
                    c +=1
            return c

        ans = None
        lo, hi = 1, len(nums)-1
        while lo < hi:
            mid = lo + ((hi-lo)>>1)
            print(lo, hi, mid)
            if count_(mid) > mid:
                hi = mid
            else:
                lo = mid + 1
        return lo


#bitwise solutionn
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        bits = n.bit_length()
        dupli = 0
        for bit in range(bits):
            mask = 1<<bit
            base_count = 0
            num_count = 0
            for i in range(n+1):
                base_count += 1 if mask & i else 0
                num_count += 1 if nums[i] & mask else 0
            if num_count > base_count:
                dupli |= (mask)
        return dupli   


#using floyds cycle detection algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast: break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow