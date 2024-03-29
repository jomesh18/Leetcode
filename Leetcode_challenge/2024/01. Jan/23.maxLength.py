'''
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

3740

265

Add to List

Share
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        memo = {}
        def helper(i, curr):
            if i == len(arr):
                ans = 0
                while curr:
                    ans += 1
                    curr &= (curr-1)
                return ans
            if (i, curr) in memo: return memo[(i, curr)]
            ans = helper(i+1, curr)
            seen = False
            new = 0
            for c in arr[i]:
                bit = 1<<(ord(c)-ord('a'))
                if (curr & bit) or (new & bit):
                    seen = True
                    break
                else:
                    new |= bit
            if not seen:
                curr |= new
                ans = max(ans, helper(i+1, curr))
            memo[(i, curr)] = ans
            return ans
        return helper(0, 0)