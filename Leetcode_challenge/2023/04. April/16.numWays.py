'''
1639. Number of Ways to Form a Target String Given a Dictionary
Hard

650

36

Add to List

Share
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.
'''
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m, k = len(words), len(target), len(words[0])
        MOD = 10**9+7
        count = [[0]*26 for _ in range(k)]
        
        for word in words:
            for i in range(k):
                count[i][ord(word[i])-ord('a')] += 1
        
        @lru_cache(None)
        def helper(tl, wl):
            if tl == m:
                return 1
            if k-wl < m-tl: return 0
            curr_tc = target[tl]
            freq = count[wl][ord(curr_tc)-ord('a')]
            ans = 1
            taking = 0
            if freq > 0:
                taking = helper(tl+1, wl+1) * freq
            not_taking = helper(tl, wl+1)
            ans = taking+not_taking
            return ans%MOD
            
        return helper(0, 0)