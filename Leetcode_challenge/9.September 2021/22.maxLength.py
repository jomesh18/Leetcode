'''
Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

 

Constraints:

    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lower case English letters.

   Hide Hint #1  
You can try all combinations and keep mask of characters you have.
   Hide Hint #2  
You can use DP.'''

class Solution:
    def maxLength(self, arr: [str]) -> int:
        # Initialize results with an empty string
        # from which to build all future results
        results = [""]
        best = 0
        for word in arr:
            # We only want to iterate through results
            # that existed prior to this loop
            for i in range(len(results)):
                # Form a new result combination and
                # use a set to check for duplicate characters
                new_res = results[i] + word
                if len(new_res) != len(set(new_res)):
                    continue

                # Add valid options to results and
                # keep track of the longest so far
                results.append(new_res)
                best = max(best, len(new_res))
        return best

arr = ["un","iq","ue"]
# Output: 4

arr = ["cha","r","act","ers"]
# # # # Output: 6
# 
arr = ["abcdefghijklmnopqrstuvwxyz"]
# # # # Output: 26

arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
# # # Output: 16

arr = ["yy","bkhwmpbiisbldzknpm"]
# # Output: 0

arr = ["a", "abc", "d", "de", "def"]
# Output: 6

sol = Solution()
print(sol.maxLength(arr))
