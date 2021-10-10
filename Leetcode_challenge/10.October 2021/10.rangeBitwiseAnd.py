'''
201. Bitwise AND of Numbers Range
Medium

1862

160

Add to List

Share
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1
'''
# naive, tle
# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         res = left
#         for num in range(left, right+1):
#             res &= num
#             if res == 0:
#                 break
#         return res

#from leetcode, bitwise
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count

left = 5
right = 7
# Output: 4

left = 0
right = 0
# # # Output: 0

left = 1
right = 2147483647
# # # Output: 0

left = 1
right = 2**31-1

left = 0b10**31-2
right = 2147483647

sol = Solution()
print(sol.rangeBitwiseAnd(left, right))
