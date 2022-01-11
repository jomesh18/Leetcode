'''
Longest Common Prefix

Solution
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
#vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        res = ""
        for c_tup in zip(*strs):
            for i in range(len(c_tup)):
                if c_tup[0] != c_tup[i]:
                    return res
            res += c_tup[0]
        return res

#from leetcode fastest, vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        idx = 0
        
        while idx < len(strs[0]):
            curr = strs[0][idx]
            for word in strs:
                if len(word) <= idx or word[idx] != curr:
                    return "".join(res)
            idx+=1
            res.append(curr)
        return "".join(res)

strs = ["flower","flow","flight"]
# Output: "fl"

# strs = ["dog","racecar","car"]
# # Output: ""

sol = Solution()
print(sol.longestCommonPrefix(strs))
