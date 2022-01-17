'''
290. Word Pattern
Easy

2578

288

Add to List

Share
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
Accepted
302,496
Submissions
769,066
'''
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         s = s.split()
#         if len(pattern) != len(s): return False
#         patt_to_s = {}
#         s_set = set()
#         for i in range(len(pattern)):
#             if pattern[i] not in patt_to_s:
#                 if s[i] in s_set: return False
#                 patt_to_s[pattern[i]] = s[i]
#                 s_set.add(s[i])
#             else:
#                 if patt_to_s[pattern[i]] != s[i]:
#                     return False
#         return True

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        ls = len(set(s))
        lp = len(set(pattern))
        return len(s) == len(pattern) and ls == lp and lp = len(set(zip(s, pattern)))

pattern = "abba"
s = "dog cat cat dog"
# Output: true

# pattern = "abba"
# s = "dog dog dog dog"
# #Output: false

# pattern = "abc"
# s = "b c a"
#Output: true

sol = Solution()
print(sol.wordPattern(pattern, s))
