'''
139. Word Break
Medium

12709

533

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
        s_count = Counter(s)
        word_count = Counter()
        trie = {}
        for word in wordDict:
            word_count += Counter(word)
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr['#'] = word
        for c in s_count:
            if c not in word_count:
                return False
        visited = [False]*(len(s)+1)
        def dfs(curr, i):
            if '#' in curr and not visited[i+1]:
                visited[i+1] = True
                to_do.append((i+1))
            if i >= len(s)-1: return False
            curr = curr.get(s[i+1], None)
            if not curr: return False
            return dfs(curr, i+1)
        
        to_do = deque([0])
        visited[0] = True
        while to_do:
            i = to_do.popleft()
            if i == len(s): return True
            if i < len(s) and s[i] in trie:
                if dfs(trie[s[i]], i):
                    return True
        return False
