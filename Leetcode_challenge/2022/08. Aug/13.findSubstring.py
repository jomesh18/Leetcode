'''
30. Substring with Concatenation of All Words
Hard

3140

2166

Add to List

Share
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
Accepted
308,597
Submissions
1,007,782
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words[0])
        word_len = len(words)
        all_count = Counter(words)
        
        def slide(left):
            curr_count = Counter()
            total_matched = 0
            
            for right in range(left, n, k):
                if right + k > n:
                    return
                curr_word = s[right: right+k]
                if curr_word not in all_count:
                    left = right + k
                    curr_count = Counter()
                    total_matched = 0
                else:
                    curr_count[curr_word] += 1
                    while curr_count[curr_word] > all_count[curr_word]:
                        old_word = s[left: left+k]
                        curr_count[old_word] -= 1
                        total_matched -= 1
                        left += k
                    total_matched += 1
                    if total_matched == word_len:
                        ans.append(left)
                    
        ans = []
        for i in range(k):
            slide(i)
        return ans