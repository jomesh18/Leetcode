'''
139. Word Break
Medium

15136

635

Add to List

Share
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
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie = {}
        for word in wordDict:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr['#'] = word
        memo = [None]*n
        def search(i):
            if i == n:
                return True
            if memo[i] is not None: return memo[i]
            curr = trie
            for k in range(i, n):
                curr = curr.get(s[k], None)
                if not curr:
                    memo[k] = False
                    return False
                if '#' in curr and search(k+1):
                    memo[k] = True
                    return True
            memo[i] = False
            return False
            
        return search(0)