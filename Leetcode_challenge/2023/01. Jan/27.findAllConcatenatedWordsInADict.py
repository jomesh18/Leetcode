'''
472. Concatenated Words
Hard

2666

243

Add to List

Share
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 105
'''
# trie solution
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr['#'] = word
        def dfs(node, word, i, count, start, from_last):
            if i == len(word):
                if count > 1 and from_last:
                    return True
                return False
            c = word[i]
            nex = node.get(c, None)
            if not nex: return False
            ans = False
            if '#' in nex:
                ans |= dfs(start, word, i+1, count+1, start, True)
            ans |= dfs(nex, word, i+1, count, start, False)
            return ans
            
        ans = []
        for word in words:
            curr = trie
            if dfs(curr, word, 0, 0, curr, False):
                ans.append(word)
                
        return ans
            
# dp O(n*m*m*m) where n is no of words and m is maxlen of word in words
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        ans = []
        for word in words:
            dp = [True] + [False]*len(word)
            for i in range(1, len(word)+1):
                for j in range(i):
                    if i != len(word) or j != 0:
                        dp[i] = dp[j] and word[j:i] in words
                        if dp[i]: break
            if dp[-1]: ans.append(word)
        return ans


#
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        def helper(i, word):
            if i == len(word):
                return True
            for end in range(i+1, len(word)+1):
                curr = word[i:end]
                if curr in words and word != curr and helper(end, word):
                    return True
            return False

        for word in words:
            if helper(0, word):
                res.append(word)
        return res