'''
1048. Longest String Chain
Medium

3936

177

Add to List

Share
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
Accepted
222,084
Submissions
380,189
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(reverse=True, key=len)
        n = len(words)
        ans = 1
        dp = [1 for _ in range(n)]
        for i in range(n):
            wordi = words[i]
            ilen = len(wordi)
            for j in range(i+1, n):
                wordj = words[j]
                jlen = len(wordj)
                if jlen == ilen: continue
                elif jlen + 1 < ilen: break
                removed = 0
                k, l = 0, 0
                while k < ilen and l < jlen and removed < 2:
                    if wordi[k] == wordj[l]:
                        l += 1
                    else:
                        removed += 1
                    k += 1
                if (k == ilen and l == jlen and removed == 1) or (k == ilen-1 and l == jlen and removed == 0):
                    dp[j] = max(dp[j], 1 + dp[i])
                    ans = max(ans, dp[j])
        return ans
 
 class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        res = 1
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i]+word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[prev]+1, dp[word])
                    res = max(dp[word], res)
        return res

# O(n*l*l)  where l is length of each word(or max len of word)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words)
        memo = {}
        def find(word):
            if word in memo: return memo[word]
            ans = 1
            for i in range(len(word)):
                prev = word[:i]+word[i+1:]
                if prev in wordSet:
                    ans = max(find(prev)+1, ans)
            memo[word] = ans
            return ans
        return max(find(word) for word in words)
