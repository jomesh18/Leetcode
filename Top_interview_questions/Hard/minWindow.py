'''
76. Minimum Window Substring
Hard

12591

579

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
        i = 0
        min_len = float('inf')
        ans = None
        start = i
        for i in range(len(s)):
            if s[i] in tcount:
                window_count[s[i]] = window_count.get(s[i], 0) + 1
                if window_count >= tcount:
                    j = start
                    while window_count >= tcount:
                        if s[j] in window_count: 
                            window_count[s[j]] -= 1
                        j += 1
                    if i-(j-1)+1 < min_len:
                        min_len = i-j+2
                        ans = (j-1, i)
                    start = j
                
        return '' if not ans else s[ans[0]: ans[1]+1]


# not comparing two dictionarys, comparing two integers
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        window_count = Counter()
        min_len = float('inf')
        ans = None
        j = 0
        formed = 0
        required = len(tcount)
        for i in range(len(s)):
            c = s[i]
            if c in tcount:
                window_count[c] = window_count.get(c, 0) + 1
                if window_count[c] == tcount[c]: formed +=1
                if formed == required:
                    while formed == required:
                        c = s[j]
                        if c in window_count: 
                            window_count[c] -= 1
                            if window_count[c] < tcount[c]:
                                formed -= 1
                        j += 1
                    if i-(j-1)+1 < min_len:
                        min_len = i-j+2
                        ans = (j-1, i)
                
        return '' if not ans else s[ans[0]: ans[1]+1]