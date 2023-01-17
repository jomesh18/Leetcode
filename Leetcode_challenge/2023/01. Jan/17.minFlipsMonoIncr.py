'''
926. Flip String to Monotone Increasing
Medium

2881

122

Add to List

Share
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
'''
'''
Approach 1: Dynamic Windows
Intuition
The result monotone increasing string can be considered as 2 consecutive non-overlapping substrings, namely, the prefix only contains character '0' and the suffix only contains character '1'. Let's consider the 2 substrings as 2 windows on the original string. Initially, the left window is empty and the right window contains the whole string. At each step, the left window's size increases by one and the right window's size decreases by 1. We want to change all the characters in the left window into '0' and all the characters in the right window into '1'.

Algorithm
We enumerate each left-right window configuration, the number of flips to make the string monotone increasing is the sum of the number of '1's in the left window and the number of '0's in the right window. Save the smallest value.



For example, in the above configuration, the number of flips to make the string monotone increasing is 4 (flip the 4 '1's in the left/green window) + 3 (flip the 3 '0's in the right/red window) = 7.

Let left1 be the number of '1's in the current left window and right0 be the number of '0's in the current right window. When the left window increases and the right window shrinks by 1 character, it means we move a character c from right to left:

If c = '0', left1 will be unchanged and right0 will be decreased by 1, so the sum of them will be decreased by 1.

If c = '1', left1 will be increased by 1 and right0 will be unchanged so the sum of them will be increased by 1.

We only need to know the result of left1 + right0, so we don't need to maintain the 2 counters separately. We can use a variable m where m = left1 + right0 implicitly.

The algorithm works as follows:

Scan the input string s to count the number of '0's in total, let it be m. This is the number of flips needed when the left window is empty and the right window is the whole string.
Set ans = m.
Scan the input string 's' again,
for each character '0', decrease m by 1 and replace ans with m if m is smaller.
for each character '1', increase m by 1.
Return ans.
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count = Counter(s)
        if '0' not in count or '1' not in count: return 0
        ans = min(count.values())
        memo = {}
        def helper(i, one_started):
            if i == len(s):
                return 0
            if (i, one_started) in memo: return memo[(i, one_started)]
            if one_started:
                if s[i] == '0':
                    ans = 1 + helper(i+1, one_started)
                else:
                    ans = helper(i+1, one_started)
            else:
                if s[i] == '1':
                    ans = 1 + helper(i+1, one_started)
                    ans = min(ans, helper(i+1, True))
                else:
                    ans = helper(i+1, one_started)
                    ans = min(ans, 1 + helper(i+1, True))
            memo[(i, one_started)] = ans
            return ans
        return helper(0, False)


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = s.count('0')
        ans = m
        for c in s:
            m += 1 if c == '1' else -1
            ans = min(ans, m)
        return ans

'''
Approach 2: Dynamic Programming
Intuition
If a string is monotone increasing, any of its prefixes are also monotone increasing. To make a prefix of length i monotone increasing, we can make the prefix of length (i - 1) monotone increasing and consider whether to flip the last character. This implies the optimization of the sub-problems which is a characteristic of Dynamic Programming.

Let dp[i] represent the minimum number of flips to make the prefix of s of length i (substring of indices [0, i)) monotone increasing.

The base case is dp[0] = 0, since an empty string is always monotone increasing. Consider dp[i] for i > 0,

If s[i - 1] = '1', then we have dp[i] = dp[i - 1], since we can always append a character '1' to the end of a monotone increasing string and it's still monotone increasing.

If s[i - 1] = '0', let's consider whether we flip it or not.

If we don't flip it, we have to flip all the '1's in s before it.
If we flip it, then we can treat it as the above case where s[i - 1] = '1' with one more flip.
In summary,

Let number num be the number of character 1s in s' prefix of length i:

dp[i] = dp[i - 1] if s[i - 1] = '1'
dp[i] = min(num, dp[i - 1] + 1) otherwise.
The final answer should be dp[s.length()]

Since dp[i] only depends on dp[i - 1], we can use a simple int variable instead of an array to reduce the space complexity.

Algorithm
Let ans be the final answer and num be the number of character 1s in the current prefix of s.

Initialize ans and num to 0.
For each character c in the input string s:
If c is 0, set ans to the minimal value of num and ans + 1.
otherwise c is 1, increase num by 1.
Return ans.
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                ans = min(ans+1, ones)
        return ans