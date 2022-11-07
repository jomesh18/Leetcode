'''
140. Word Break II
Hard

5580

493

Add to List

Share
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Accepted
489,683
Submissions
1,101,282
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dic = {key: i for i, key in enumerate(wordDict)}
        self.ans = []
        def helper(start, temp):
            if start == len(s):
                self.ans.append(' '.join([wordDict[i] for i in temp]))
                return
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in word_dic:
                    helper(end, temp+[word_dic[word]])
            
        helper(0, [])
        return self.ans