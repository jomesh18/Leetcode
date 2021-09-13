'''
Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 

Constraints:

    1 <= text.length <= 104
    text consists of lower case English letters only.

'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for c in text:
            d[c] = d.get(c, 0) + 1
        max_count = float("inf")
        for c in "ban":
            temp_count = d.get(c, 0)
            if temp_count < max_count:
                max_count = temp_count
        for c in "lo":
            temp_count = d.get(c, 0)
            temp_count //= 2
            if temp_count < max_count:
                max_count = temp_count
        return max_count

#from leetcode
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         d = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        
#         for ch in text:
#             if ch in d:
#                 d[ch] += 1 if ch in ('l', 'o') else 2
        
#         return min(d.values()) // 2

text = "nlaebolko"
# Output: 1

text = "loonbalxballpoon"
# # Output: 2

text = "leetcode"
# # Output: 0

text = "balon"
# Output: 0

text = "lloo"
# Output: 0

sol = Solution()
print(sol.maxNumberOfBalloons(text))
