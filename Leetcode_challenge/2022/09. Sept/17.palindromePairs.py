'''
336. Palindrome Pairs
Hard

3936

411

Add to List

Share
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
 

Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
Accepted
183,348
Submissions
519,332
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = {}
        for i, word in enumerate(words):
            curr = trie
            for c in reversed(word):
                curr = curr.setdefault(c, {})
            curr['#'] = i
        
        def dfs(s, curr, res, i):
            if '#' in curr and curr['#'] != i and s == s[::-1]:
                    res.append([i, curr['#']])
            for c in curr:
                if c != '#':
                    dfs(s+c, curr[c], res, i)
                
        def search(word, curr, res, i):
            for j, c in enumerate(word):
                if '#' in curr:
                    temp = word[j:]
                    if temp == temp[::-1]:
                        res.append([i, curr['#']])
                curr = curr.get(c, None)
                if not curr: return res
            dfs("", curr, res, i)
            return res
            
        ans = []
        for i, word in enumerate(words):
            curr = trie
            res = []
            search(word, curr, res, i)
            ans.extend(res)
        return ans

#O(n*k*k) where k is avg len of word in words
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                pre, suf = word[:j], word[j:]
                if pre[::-1] in d and d[pre[::-1]] != i and suf == suf[::-1]:
                    res.append([i, d[pre[::-1]]])
                if j != 0 and suf[::-1] in d and d[suf[::-1]] != i and pre == pre[::-1]:
                    res.append([d[suf[::-1]], i])
        return res