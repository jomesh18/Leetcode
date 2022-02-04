'''
Word Break

Solution
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
#dp solution
# class Solution:
#     def wordBreak(self, s: str, wordDict: [str]) -> bool:
#         dp = [False] * len(s)

#         for i in range(len(s)):
#             for word in wordDict:
#                 if s[i] == word[-1]:
#                     l = len(word)
#                     if i - l >= -1 and s[i-l+1:i+1] == word:
#                         if i - l == -1:
#                             dp[i] = True
#                         else:
#                             dp[i] = dp[i] or dp[i-l]
#         print(dp)
#         return dp[-1]

#memoization
class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        memo = {}
        def helper(i):
            if i < -1:
                return False
            if i in memo: return memo[i]
            ans = False
            for word in wordDict:
                l = len(word)
                if s[i] == word[-1]:
                    if i - l >= -1 and s[i-l+1:i+1] == word:
                        if i-l == -1:
                            return True
                        else:
                            ans = ans or helper(i-l)
            memo[i] = ans
            return ans
            
        return helper(len(s)-1)

s = "leetcode"
wordDict = ["leet","code"]
# Output: true

# s = "applepenapple"
# wordDict = ["apple","pen"]
# # Output: true

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# # # Output: false

# s = "dogs"
# wordDict = ["dog","s","gs"]
# Output: true

s = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# False


sol = Solution()
print(sol.wordBreak(s, wordDict))
