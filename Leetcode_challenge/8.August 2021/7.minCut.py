'''
Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:

Input: s = "a"
Output: 0

Example 3:

Input: s = "ab"
Output: 1

 

Constraints:

    1 <= s.length <= 2000
    s consists of lower-case English letters only.

'''
class Solution:
    def minCut(self, s: str) -> int:
        cut = [x for x in range(-1,len(s))]
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[-1]

s = "aab"
# Output: 1

s = "a"
# # Output: 0

s = "ab"
# # Output: 1

sol = Solution()
print(sol.minCut(s))
