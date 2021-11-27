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
class Solution:
    """
    @param strings: a string array
    @return: return a list of string array
    """
    def groupStrings(self, strings):
        # write your code here
        