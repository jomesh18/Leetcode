'''
Lintcode
922 · Group Shifted Strings
Algorithms
Medium
Accepted Rate67%
Description
Solution
Notes
Discuss
Leaderboard
Description

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

You don't need to care about the order of the result.
Example

Example 1:

input:["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

output: [["a","z"],["abc","bcd","xyz"],["acef"],["az","ba"]]

Example 2:

input:["a"]

output:[["a"]]
'''
from collections import defaultdict
class Solution:
    """
    @param strings: a string array
    @return: return a list of string array
    """
    def groupStrings(self, strings):
        # write your code here
        def find_diff(s):
            key = []
            for i in range(1, len(s)):
                key.append(str((ord(s[i])-ord(s[i-1]))%26))
            if not key: key = ["0"]
            return ",".join(key)
    
        d = defaultdict(list)
        for s in strings:
            d[find_diff(s)].append(s)
        
        res = []
        for vals in d.values():
            res.append(vals)
        return res


#from lintcode
class Solution:
    """
    @param strings: a string array
    @return: return a list of string array
    """
    def groupStrings(self, strings):
        # write your code here
        res = {}
        for s in strings:
            n = len(s)
            if n <= 1:
                res[(n,)] = res.get((n,), []) + [s]
                continue
            key = [n]
            for i in range(1, len(s)): key.append((ord(s[i]) - ord(s[i - 1]) + 26) % 26)
            key = tuple(key)
            res[key] = res.get(key, []) + [s]
        return [_ for _ in res.values()]


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
output = [["a","z"],["abc","bcd","xyz"],["acef"],["az","ba"]]

strings = ["a"]
output = [["a"]]

sol = Solution()
print(sol.groupStrings(strings))
