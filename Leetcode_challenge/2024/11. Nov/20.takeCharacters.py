'''
2516. Take K of Each Character From Left and Right
Medium

1367

157

Add to List

Share
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
'''
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0]*3
        for c in s:
            count[ord(c)-ord('a')] += 1
        for c in count:
            if c < k:
                return -1
        left, max_window = 0, 0
        curr_window = [0]*3
        for right in range(n):
            curr_window[ord(s[right])-ord('a')] += 1
            while left <= right and (count[0] - curr_window[0] < k or count[1] - curr_window[1] < k or count[2] - curr_window[2] < k):
                curr_window[ord(s[left])-ord('a')] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return n - max_window