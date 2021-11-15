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
        c_dict = {}
        for c in s:
            c_dict[c] = c_dict.setdefault(c, 0) + 1
        for i, c in enumerate(s):
            if c_dict.get(c) == 1:
                return i
        return -1


#from leetcode, fastest
class Solution:
    def firstUniqChar(self, s: str) -> int:
        min_unique_char_index = len(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            i = s.find(c)
            if i != -1 and i == s.rfind(c):
                min_unique_char_index = min(min_unique_char_index, i)
        return min_unique_char_index if min_unique_char_index != len(s) else -1
