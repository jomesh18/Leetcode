'''
451. Sort Characters By Frequency
Medium

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

 

Constraints:

    1 <= s.length <= 5 * 105
    s consists of uppercase and lowercase English letters and digits.

'''
from collections import Counter
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         freq_dict = Counter(s)
#         res = [(freq_dict[key], key) for key in freq_dict]
#         res.sort(key = lambda x: -x[0])
#         res = [x[1]*x[0] for x in res]
#         return "".join(res)

#from leetcode
class Solution:
    def frequencySort(self, s: str) -> str:      
        d1, d2 = Counter(s), {}
        for key, val in d1.items():
            d2.setdefault(val, []).append(key*val)
        print(d2)
        return "".join(["".join(d2[i]) for i in range(len(s), 0, -1) if i in d2])

s = "tree"
# Output: "eert"

# s = "cccaaa"
# Output: "aaaccc"

# s = "Aabb"
# Output: "bbAa"

sol = Solution()
print(sol.frequencySort(s))
