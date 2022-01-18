'''
Delete and Earn

Solution
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        def helper(to_do, curr_score):
            if (to_do, curr_score) in memo: return memo[(to_do, curr_score)]
            if len(to_do) == 1:
                elem = to_do.pop()
                curr_score += elem*d[elem]
                to_do.add(elem)
                return curr_score
            ans = 0    
            for i in to_do:
                flag1, flag2 = False, False
                to_do.remove(i)
                curr_score += i*d[i]
                if i+1 in to_do: 
                    flag1 = True
                    to_do.remove(i+1)
                if i-1 in to_do:
                    flag2 = True
                    to_do.remove(i-1)
                ans = max(ans, helper(to_do, curr_score))
                if flag1: to_do.add(i+1)
                if flag2: to_do.add(i-1)
                to_do.add(i)
                curr_score -= i*d[i]
            memo[(to_do, curr_score)] = ans
            return ans

        return helper(set(nums), 0)


nums = [3,4,2]
# Output: 6

# nums = [2,2,3,3,3,4]
# Output: 9

nums = [12,32,93,17,100,72,40,71,37,92,58,34,29,78,11,84,77,90,92,35,12,5,27,92,91,23,65,91,85,14,42,28,80,85,38,71,62,82,66,3,33,33,55,60,48,78,63,11,20,51,78,42,37,21,100,13,60,57,91,53,49,15,45,19,51,2,96,22,32,2,46,62,58,11,29,6,74,38,70,97,4,22,76,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93]
# Output: 

print(len(nums))

sol = Solution()
print(sol.deleteAndEarn(nums))
