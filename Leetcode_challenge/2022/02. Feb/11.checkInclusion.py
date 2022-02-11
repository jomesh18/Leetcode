'''
567. Permutation in String
Medium

4754

130

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
Accepted
310,480
Submissions
696,030
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = Counter(s1)
        S2 = Counter(s2[:len(s1)])
        if S1 == S2: return True
        for i in range(1, len(s2)-len(s1)+1):
            S2[s2[i-1]] -= 1
            if S2[s2[i-1]] == 0: S2.pop(s2[i-1])
            S2[s2[i+len(s1)-1]] += 1
            if S1 == S2: return True
            
        return False

