'''
Partition Array into Disjoint Intervals

Given an array nums, partition it into two (contiguous) subarrays left and right so that:

    Every element in left is less than or equal to every element in right.
    left and right are non-empty.
    left has the smallest possible size.

Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]

 

Note:

    2 <= nums.length <= 30000
    0 <= nums[i] <= 106
    It is guaranteed there is at least one way to partition nums as described.
'''

class Solution:
    def partitionDisjoint(self, nums: [int]) -> int:
        num_dict = {len(nums)-1: nums[-1]}
        for i in range(len(nums)-2, -1, -1):
            num_dict[i] = nums[i] if nums[i] < num_dict[i+1] else num_dict[i+1]
        # print(num_dict)
        largest = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > largest:
                largest = nums[i]
            if largest <= num_dict[i+1]:
                return i+1

nums = [5,0,3,8,6]
# Output: 3

nums = [1,1,1,0,6,12]
# Output: 4

nums = [1,1]
#Output: 1

nums = [26,51,40,58,42,76,30,48,79,91]
#Output: 1

s = Solution()
print(s.partitionDisjoint(nums))
