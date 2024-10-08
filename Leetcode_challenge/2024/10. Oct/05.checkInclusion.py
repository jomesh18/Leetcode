'''
567. Permutation in String
Medium

11886

449

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
        s1_count, s2_count = Counter(s1), Counter(s2)
        for key in s1_count:
            if key not in s2_count or s1_count[key] > s2_count[key]:
                return False
        copied_s1_count = s1_count.copy()
        found = 0
        l = 0
        for i in range(len(s2)):
            c = s2[i]
            if copied_s1_count[c] == 0:
                while s2[l] != s2[i]: 
                    copied_s1_count[s2[l]] += 1
                    found -= 1
                    l += 1
                l += 1
            else:
                copied_s1_count[c] -= 1
                found += 1
                if found == len(s1):
                    return True
        return False