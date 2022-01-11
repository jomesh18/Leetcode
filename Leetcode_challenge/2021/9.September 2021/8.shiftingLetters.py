'''
Shifting Letters

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

    For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

 

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    shifts.length == s.length
    0 <= shifts[i] <= 109

'''
class Solution:
    def shiftingLetters(self, s: str, shifts: [int]) -> str:
        ans = []
        X = sum(shifts) % 26
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26

        return "".join(ans)


# class Solution:
#     def shiftingLetters(self, s: str, shifts: [int]) -> str:
#         ans = []
#         def shift(c, n):
#             temp = ((ord(c) + n) % 123)
#             if temp < 97:
#                 temp += 97
#             return chr(temp)
#         count = 0
#         for i in range(len(s)-1, -1, -1):
#             count += shifts[i]
#             ans.append(shift(s[i], count))
#         return "".join(ans)[::-1]
        

# s = "abc"
# shifts = [3,5,9]
# # Output: "rpl"

s = "aaa"
shifts = [1,2,3]
# # Output: "gfd"

sol = Solution()
print(sol.shiftingLetters(s, shifts))
