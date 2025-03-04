'''
1780. Check if Number is a Sum of Powers of Three
Solved
Medium
Topics
Companies
Hint
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107
'''
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        items = []
        item = 1
        while item <= n:
            items.append(item)
            item *= 3

        def helper(arr, i, s):
            if s == n:
                return True
            if i == len(arr) or s > n:
                return False
            return helper(arr, i+1, s+arr[i]) or helper(arr, i+1, s)

        return helper(items, 0, 0)
