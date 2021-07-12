'''
 Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

 

Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c_map = {}
        for c1, c2 in zip(s, t):
            if c1 in c_map:
                if not c_map[c1] == c2:
                    return False
            elif c2 in c_map.values():
                return False
            else:
                c_map[c1] = c2
        return True

s = "egg"
t = "add"
# Output: true

# s = "foo"
# t = "bar"
# Output: false

# s = "paper"
# t = "title"
# Output: true

s = "badc"
t = "baba"
# Output = False

sol = Solution()
print(sol.isIsomorphic(s, t))
