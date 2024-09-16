'''
1371. Find the Longest Substring Containing Vowels in Even Counts
Medium

2342

119

Add to List

Share
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefix_xor = 0
        character_map = [0]*26
        for i, c in enumerate('aeiou'):
            character_map[ord(c)-ord('a')] = 1 << i
        first_occurance = [-1]*32
        longest_substring = 0
        for i, c in enumerate(s):
            prefix_xor ^= character_map[ord(c)-ord('a')]
            if first_occurance[prefix_xor] == -1 and prefix_xor != 0:
                first_occurance[prefix_xor] = i
            longest_substring = max(longest_substring, i-first_occurance[prefix_xor])
        return longest_substring