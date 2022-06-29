'''
1647. Minimum Deletions to Make Character Frequencies Unique
Medium

2032

39

Add to List

Share
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
Accepted
115,236
Submissions
198,219
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        vals = set()
        c = 0
        for v in count.values():
            if v not in vals:
                vals.add(v)
            else:
                for i in range(v, 0, -1):
                    if i not in vals:
                        vals.add(i)
                        break
                    c += 1
        return c

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = list(Counter(s).values())
        freq.sort(reverse=True)
        max_allowable_freq = len(s)
        count = 0
        # print(freq)
        for f in freq:
            # print(f, max_allowable_freq, count)
            if f > max_allowable_freq:
                count += f-max_allowable_freq
            max_allowable_freq = min(max_allowable_freq, f) - 1
            if max_allowable_freq < 0: max_allowable_freq = 0
            # print(f, max_allowable_freq, count)
        return count

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0]*26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        freq.sort(reverse=True)
        max_allowable_freq = len(s)
        count = 0
        for f in freq:
            if f > max_allowable_freq:
                count += f-max_allowable_freq
                f = max_allowable_freq
            max_allowable_freq = max(0, f-1)
        return count