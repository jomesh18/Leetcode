'''
76. Minimum Window Substring
Hard

17310

701

Add to List

Share
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

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
        m, n = len(s), len(t)
        t_c = Counter(t)
        curr_c = Counter()
        ans = [0, m]
        completed = 0
        start = 0
        for i in range(m):
            if s[i] in t_c:
                curr_c[s[i]] += 1
                if curr_c[s[i]] == t_c[s[i]]:
                    completed += 1
                if completed == len(t_c):
                    while start <= i-n:
                        if s[start] not in t_c or curr_c[s[start]] > t_c[s[start]]:
                            if curr_c[s[start]] > t_c[s[start]]:
                                curr_c[s[start]] -= 1
                            start += 1
                        else:
                            break
                    if ans[1]-ans[0] > i-start:
                        ans = [start, i]
        return "" if ans == [0, m] else s[ans[0]: ans[1]+1]