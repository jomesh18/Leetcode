'''
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

2403

178

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
        def backtrack(i, mask):
            if (i, mask) in memo: return memo[(i, mask)]
            if i == len(arr): return 0
            ans = backtrack(i+1, mask)
            add = True
            new = 0
            for c in arr[i]:
                bit = (1<<(ord(c)-ord('a')))
                if (new & bit) or (mask & bit):
                    add = False
                    break
                new |= bit
            if add:
                ans = max(ans, len(arr[i]) + backtrack(i+1, mask ^ new))
            memo[(i, mask)] = ans
            return ans

        return backtrack(0, 0)

#using set
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for s in arr:
            if len(set(s)) != len(s): continue
            s = set(s)
            for c in dp[:]:
                if s & c: continue
                dp.append(s|c)
        return max(len(c) for c in dp)

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [""]
        best = 0
        for word in arr:
            for i in range(len(res)):
                new_word = word+res[i]
                if len(new_word) != len(set(new_word)): continue
                res.append(new_word)
                best = max(best, len(new_word))
        return best