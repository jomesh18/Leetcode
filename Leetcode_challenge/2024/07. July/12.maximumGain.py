'''
1717. Maximum Score From Removing Substrings
Medium

891

64

Add to List

Share
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
        stack = []
        ans = 0
        # remove ab first
        for c in s:
            if c == 'b' and stack and stack[-1] == 'a':
                stack.pop()
                ans += x
            else:
                stack.append(c)
        # print(ans)

        stack2 = []
        for c in stack:
            if c == 'a' and stack2 and stack2[-1] == 'b':
                stack2.pop()
                ans += y
            else:
                stack2.append(c)
        # print(ans)

        curr = ans
        ans = 0
        
        stack = []
        # remove ab first
        for c in s:
            if c == 'a' and stack and stack[-1] == 'b':
                stack.pop()
                ans += y
            else:
                stack.append(c)
        # print(ans)

        stack2 = []
        for c in stack:
            if c == 'b' and stack2 and stack2[-1] == 'a':
                stack2.pop()
                ans += x
            else:
                stack2.append(c)
        # print(ans)

        return max(curr, ans)



class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_pair = 'ab' if x > y else 'ba'
        max_points = x if max_pair == 'ab' else y
        min_points = x if max_pair != 'ab' else y
        stack = []
        ans = 0

        for c in s:
            if c == max_pair[1] and stack and stack[-1] == max_pair[0]:
                stack.pop()
                ans += max_points
            else:
                stack.append(c)

        stack2 = []
        for c in stack:
            if c == max_pair[0] and stack2 and stack2[-1] == max_pair[1]:
                stack2.pop()
                ans += min_points
            else:
                stack2.append(c)

        return ans