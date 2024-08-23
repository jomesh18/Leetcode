'''
650. 2 Keys Keyboard
Medium

4167

242

Add to List

Share
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
'''
class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def helper(curr_total, last_copied):
            if curr_total == n:
                return 0
            if curr_total > n:
                return float('inf')
            if (curr_total, last_copied) in memo: return memo[(curr_total, last_copied)]
            paste_only, copied_and_paste = float('inf'), float('inf')
            # paste only
            if last_copied:
                paste_only = 1 + helper(curr_total+last_copied, last_copied)
            # copy and paste
            copied_and_paste = 2 + helper(curr_total * 2, curr_total)
            memo[(curr_total, last_copied)] = min(paste_only, copied_and_paste)
            return memo[(curr_total, last_copied)]
        return helper(1, 0)