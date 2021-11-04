'''
	567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#     	target = [0] * 26
#     	for c in s1:
#     		target[ord(c)-ord('a')] += 1
#     	window = [0] * 26
#     	for i, c in enumerate(s2):
#     		window[ord(c)-ord('a')] += 1
#     		if i >= len(s1):
#     			window[ord(s2[i-len(s1)])-ord('a')] -= 1
#     		if target == window:
#     			return True
#     	return False

from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        for c in s1:
            s1_count[c] += 1
        last = len(s1)
        for c in s2[:last]:
            s2_count[c] += 1
        first = 0
        while last < len(s2):
            if s1_count == s2_count:
                return True
            s2_count[s2[first]] -= 1
            if s2_count[s2[first]] < 1: del s2_count[s2[first]]
            s2_count[s2[last]] += 1
            first += 1
            last += 1
        return s1_count == s2_count


s1 = "ab"
s2 = "eidbaooo"
# Output: true

# s1 = "ab"
# s2 = "eidboaoo"
# Output: false

sol = Solution()
print(sol.checkInclusion(s1, s2))

