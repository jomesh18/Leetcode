'''
567. Permutation in String
Medium

8395

273

Add to List

Share
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        c1 = Counter(s1)
        c2 = Counter(s2[:n1])
        if c1 == c2: return True
        for i in range(n1, n2):
            c2[s2[i]] += 1
            c2[s2[i-n1]] -= 1
            if c1 == c2: return True
        return False