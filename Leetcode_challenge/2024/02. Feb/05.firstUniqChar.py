'''
387. First Unique Character in a String
Easy

8502

278

Add to List

Share
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = i
            else:
                count[s[i]] = len(s)
        ans = len(s)
        for c in count:
            if count[c] < ans:
                ans = count[c]
        return ans if ans != len(s) else -1