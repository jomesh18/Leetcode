'''
345. Reverse Vowels of a String
Easy

2479

2157

Add to List

Share
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        d = 'aeiouAEIOU'
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            while i < j and s[i] not in d:
                i += 1
            while j > i and s[j] not in d:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)