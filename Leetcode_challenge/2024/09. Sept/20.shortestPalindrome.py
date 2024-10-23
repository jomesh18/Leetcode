'''
214. Shortest Palindrome
Hard

4248

273

Add to List

Share
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        hash_base = 29
        mod_value = 10**9+7
        forward_hash = 0
        reverse_hash = 0
        power_value = 1
        palindromic_end_index = -1
        for i, curr_char in enumerate(s):
            forward_hash = (forward_hash * hash_base + (ord(curr_char) - ord('a') + 1) ) % mod_value
            reverse_hash = (reverse_hash + (ord(curr_char) - ord('a') + 1)*power_value) % mod_value
            
            if forward_hash == reverse_hash:
                palindromic_end_index = i
            power_value = (power_value * hash_base) % mod_value
        return s[palindromic_end_index+1:][::-1]+s