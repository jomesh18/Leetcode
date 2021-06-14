'''
 Find Smallest Letter Greater Than Target

Solution
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"
 

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
   Show Hint #1  
Try to find whether each of 26 next letters are in the given string array.

'''

# my try, using bisect
# import bisect
# class Solution:
#     def nextGreatestLetter(self, letters: [str], target: str) -> str:
#         pos = bisect.bisect_right(letters, target)
        # return letters[pos] if pos < len(letters) else letters[0]
        # return letters[pos % len(letters)]

#my try, not using bisect
class Solution:
    def nextGreatestLetter(self, letters: [str], target: str) -> str:
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = (lo+hi)//2
            if target < letters[mid]: hi = mid
            else: lo = mid + 1
        # return letters[lo] if lo < len(letters) else letters[0]
        return letters[lo%len(letters)]

letters = ["c","f","j"]
target = "a"
# Output: "c"

letters = ["c","f","j"]
target = "c"
# # Output: "f"

letters = ["c","f","j"]
target = "d"
# # Output: "f"

letters = ["c","f","j"]
target = "g"
# # Output: "j"

letters = ["c","f","j"]
target = "j"
# Output: "c"

s = Solution()
print(s.nextGreatestLetter(letters, target))
