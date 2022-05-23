'''
474. Ones and Zeroes
Medium

3116

338

Add to List

Share
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
Accepted
114,857
Submissions
254,418
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        memo = {}
        
        def helper(i, m, n):
            if i == len(strs): return 0
            if m < 0 or n < 0: return 0
            if (i, m, n) in memo: return memo[(i, m, n)]
            #not taking
            ans1 = helper(i+1, m, n)
            #taking
            ans2 = 0
            
            zeroes = strs[i].count("0")
            ones = len(strs[i]) - zeroes
            if zeroes <= m and ones <= n:
                ans2 = 1 + helper(i+1, m-zeroes, n-ones)
                
            ans = max(ans1, ans2)
            memo[(i, m, n)] = ans
            return ans
        
        return helper(0, m, n)
            