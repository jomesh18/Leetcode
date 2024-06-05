'''
1002. Find Common Characters
Easy

3861

338

Add to List

Share
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for word in words[1:]:
            curr_count = Counter(word)
            for key, val in count.items():
                count[key] = min(count.get(key, 0), curr_count.get(key, 0))
        ans = []
        for key, val in count.items():
            for i in range(val):
                ans.append(key)
        return ans
