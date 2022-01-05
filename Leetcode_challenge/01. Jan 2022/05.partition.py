'''
131. Palindrome Partitioning
Medium

5336

158

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
Accepted
390,832
Submissions
684,312
'''
class Solution:
    def partition(self, s: str) -> [[str]]:
        def is_palindrome(beg, end):
            while beg < end:
                if s[beg] != s[end]:
                    return False
                beg += 1
                end -= 1
            return True
        self.res = []
        def dfs(temp_res, beg, end, inserted):
            if end == len(s):
                if inserted:
                    self.res.append(temp_res)
                return
            
            if is_palindrome(beg, end):
                dfs(temp_res+[s[beg:end+1]], end+1, end+1, True)
            dfs(temp_res, beg, end+1, False)
                
        dfs([], 0, 0, False)
        return self.res

s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# s = "a"
# Output: [["a"]]

# s = "aababaabbaababaa"

sol = Solution()
print(sol.partition(s))
