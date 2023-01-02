'''
290. Word Pattern
Easy

5582

645

Add to List

Share
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        rev_d = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for u, v in zip(pattern, s):
            if u in d and d[u] != v: return False
            elif v in rev_d and rev_d[v] != u: return False
            else:
                d[u] = v
                rev_d[v] = u
        return True

# hashtable and set O(n), O(n)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split()
        seen = [0]*26
        if len(s) != len(pattern): return False
        for i in range(len(pattern)):
            curr, c = s[i], pattern[i]
            if curr in d:
                if d[curr] != c: return False
            elif seen[ord(c)-ord('a')]:
                return False
            else:
                d[curr] = c
                seen[ord(c)-ord('a')] = 1
        return True