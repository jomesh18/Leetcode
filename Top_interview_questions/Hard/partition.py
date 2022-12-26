'''
Palindrome Partitioning

Solution
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        starts_at = [[] for _ in range(n)]
        ans = []
        def dfs(i, curr):
            if i == n:
                ans.append(curr)
                return
            for k in starts_at[i]:
                dfs(i+k, curr+[s[i:i+k]])
        for i in range(n):
            for j in range(i+1, n+1):
                curr = s[i:j]
                if curr == curr[::-1]:
                    starts_at[i].append(j-i)
        dfs(0, [])
        return ans