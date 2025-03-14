'''
3306. Count of Substrings Containing Every Vowel and K Consonants II
Solved
Medium
Topics
Companies
Hint
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5
'''
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        consonants = 0
        vowels = {}
        n = len(word)
        next_consonant = [n]*n
        ind = n
        l = 0
        for i in range(n-1, -1, -1):
            next_consonant[i] = ind
            if word[i] not in 'aeiou':
                ind = i
        
        ans = 0
        for r in range(n):
            if word[r] in 'aeiou':
                vowels[word[r]] = vowels.get(word[r], 0) + 1
            else:
                consonants += 1
                while consonants > k:
                    if word[l] in 'aeiou':
                        vowels[word[l]] -= 1
                        if vowels[word[l]] == 0:
                            del vowels[word[l]]
                    else:
                        consonants -= 1
                    l += 1
            while len(vowels) == 5 and consonants == k:
                ans += next_consonant[r] - r
                if word[l] in 'aeiou':
                    vowels[word[l]] -= 1
                    if vowels[word[l]] == 0:
                        del vowels[word[l]]
                else:
                    consonants -= 1
                l += 1
        
        return ans