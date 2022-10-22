'''
76. Minimum Window Substring
Hard

12837

578

Add to List

Share
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        window_count = Counter()
        required = len(tcount)
        formed = 0
        ans = (float('inf'), 0, len(s))
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in tcount:
                window_count[c] = window_count.get(c, 0) + 1
                if window_count[c] == tcount[c]: formed += 1
                if formed == required:
                    while formed == required:
                        c = s[l]
                        if c in tcount:
                            window_count[c] -= 1
                            if window_count[c] < tcount[c]:
                                formed -= 1
                        l += 1
                    if r-(l-1)+1 < ans[0]:
                        ans = r-(l-1)+1, l-1, r
        
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2]+1]