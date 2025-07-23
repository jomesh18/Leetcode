'''
1717. Maximum Score From Removing Substrings
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.

'''
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def find(c, v, stack, s):
            ans = 0
            for ch in s:
                if ch in c[1]:
                    if stack and stack[-1] == c[0]:
                        stack.pop()
                        ans += v
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
            return ans
        
        stack = []
        ans1 = find('ab', x, stack, s)
        ans1 += find('ba', y, [], stack)

        stack = []
        ans2 = find('ba', y, stack, s)
        ans2 += find('ab', x, [], stack)

        return max(ans1, ans2)
