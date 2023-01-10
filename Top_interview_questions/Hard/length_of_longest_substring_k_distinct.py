'''
https://www.lintcode.com/problem/386/
386 · Longest Substring with At Most K Distinct Characters
Algorithms
Medium
Accepted Rate
31%
Description
Solution67
Notes99+
Discuss9
Leaderboard
Record
Description
Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Wechat reply 【Google】 get the latest requent Interview questions. (wechat id : jiuzhang1104)


Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"
Challenge
O(n) time
'''
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        ans, l, d = 0, 0, {}
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            while len(d) > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            ans = max(ans, r-l+1)
        return ans