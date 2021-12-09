'''
First Unique Character in a String

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
        duplicate = set()
        d = {}
        for i, c in enumerate(s):
            if c not in duplicate:
                if c in d:
                    duplicate.add(c)
                    del d[c]
                else:
                    d[c] = i
        if len(d) == 0: return -1
        ans = len(s)
        for key, val in d.items():
            ans = min(ans, val)
        return ans

# O(n), O(1) (since alphabets are of len 26)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, val in enumerate(s):
            if count[val] == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        d = {}
        for idx, c in enumerate(s):
            if c not in seen:
                d[c] = idx
                seen.add(c)
            elif c in d:
                del d[c]
        return min(d.values) if d else -1
