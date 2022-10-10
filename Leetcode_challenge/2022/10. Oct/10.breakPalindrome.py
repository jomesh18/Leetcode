'''
1328. Break a Palindrome
Medium

1152

536

Add to List

Share
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
 

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
'''
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ""
        count = Counter(palindrome)
        # print(count, n)
        if count['a'] == n or count['a'] == n-1:
            i = palindrome.rfind('a')
            return palindrome[:i]+'b'+palindrome[i+1:]
        else:
            for i in range(len(palindrome)):
                if palindrome[i] != 'a':
                    return palindrome[:i]+'a'+palindrome[i+1:]


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b' if palindrome[:-1] else ''