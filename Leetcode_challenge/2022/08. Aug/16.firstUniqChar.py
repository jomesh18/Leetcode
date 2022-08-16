'''
387. First Unique Character in a String
Easy

5912

217

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
Accepted
1,159,192
Submissions
1,995,247
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        once = {key for key in count if count[key] == 1}
        if not once: return -1
        for i, c in enumerate(s):
            if c in once:
                return i

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1