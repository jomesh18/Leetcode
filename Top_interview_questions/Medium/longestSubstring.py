'''
395. Longest Substring with At Least K Repeating Characters
Medium

4973

403

Add to List

Share
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0
        count = Counter(s)
        to_remove = set(c for c in count if count[c] < k)
        if not to_remove: return len(s)
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in to_remove:
                ans = max(ans, self.longestSubstring(s[l:r], k))
                l = r+1
        return max(ans, self.longestSubstring(s[l:], k))


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def helper(start, end, k):
            if end <= start: return 0
            count = [0]*26
            for i in range(start, end):
                count[ord(s[i])-ord('a')] += 1
            for i in range(start, end):
                if count[ord(s[i])-ord('a')] >= k: continue
                nextstart = i
                while nextstart < end and count[ord(s[nextstart])-ord('a')] < k: nextstart += 1
                return max(helper(start, i, k), helper(nextstart, end, k))
            return end-start

        return helper(0, len(s), k)


# sliding window
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for curr_unique in range(1, len(set(s))+1):
            count_map = [0]*26
            start = 0
            end = 0
            unique = 0
            count_above_k = 0
            while end < len(s):
                
                if unique <= curr_unique:
                    idx = ord(s[end])-ord('a')
                    if not count_map[idx]: unique += 1
                    count_map[idx] += 1
                    if count_map[idx] == k: count_above_k += 1
                    end += 1
                else:
                    idx = ord(s[start])-ord('a')
                    if count_map[idx] == k: count_above_k -= 1
                    count_map[idx] -= 1
                    if not count_map[idx]: unique -= 1
                    start += 1
                if unique == curr_unique and count_above_k == unique:
                    ans = max(ans, end-start)
        return ans