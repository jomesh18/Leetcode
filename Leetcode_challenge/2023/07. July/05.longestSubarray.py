'''
1493. Longest Subarray of 1's After Deleting One Element
Medium

2342

44

Add to List

Share
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        del_pos = (False, 0)
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]:
                count += 1
            else:
                if del_pos[0]:
                    ans = max(ans, count)
                    count = i-del_pos[1]-1
                del_pos = (True, i)
            # print(i, ans, count, del_pos)
        ans = max(count, ans)
        return ans if ans < len(nums) else ans-1