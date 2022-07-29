'''
890. Find and Replace Pattern
Medium

2428

132

Add to List

Share
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
 

Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
Accepted
118,926
Submissions
155,241
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def check(word):
            if len(word) != len(pattern): return False
            found = set()
            d = {}
            for c1, c2 in zip(word, pattern):
                if c2 in found:
                    if c1 not in d or d[c1] != c2: return False
                if c1 in d:
                    if d[c1] != c2: return False
                else:
                    d[c1] = c2
                    found.add(c2)
            return True

        return [word for word in words if check(word)]