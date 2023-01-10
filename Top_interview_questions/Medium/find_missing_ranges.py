'''641 · Missing Ranges
Algorithms
Medium
Accepted Rate
25%
Description
Solution17
Notes99+
Discuss6
Leaderboard
Record
Description
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example
Example 1

Input:
nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
Output:
["2", "4->49", "51->74", "76->99"]
Explanation:
in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]
Example 2

Input:
nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
Output:
["4->6"]
Explanation:
in range[0,7],the missing range include range[4,6]
'''
https://www.lintcode.com/problem/641/
from typing import (
    List,
)

class Solution:
    """
    @param nums: a sorted integer array
    @param lower: An integer
    @param upper: An integer
    @return: a list of its missing ranges
    """
    def find_missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # write your code here
        if not nums:
            return [str(lower)+'->'+str(upper)] if lower != upper else [str(lower)]
        ans = []
        if nums[0] != lower:
            ans.append(str(lower)+'->'+str(nums[0]-1) if lower != nums[0]-1 else str(lower))
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] != nums[i-1]+1:
                ans.append(str(nums[i]-1) if nums[i-1]+1 == nums[i]-1 else str(nums[i-1]+1)+"->"+str(nums[i]-1))
        if nums[-1] != upper:
            ans.append(str(nums[-1]+1)+'->'+str(upper) if nums[-1]+1 != upper else str(upper))
        return ans