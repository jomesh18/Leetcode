'''
1647. Minimum Deletions to Make Character Frequencies Unique
Medium

4755

71

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
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        # print(count)
        freq_count = Counter(count.values())
        # print(freq_count)
        l = sorted(freq_count.keys())[::-1]
        # print(l)
        can_be_used = set()
        last = 0
        for v in l[::-1]:
            for curr in range(v-1, last, -1):
                can_be_used.add(curr)
            last = v
        can_be_used = sorted(list(can_be_used))
        # print(can_be_used)
        ans = 0
        for freq in l:
            while freq_count[freq] > 1:
                while can_be_used and freq < can_be_used[-1]:
                    can_be_used.pop()
                if can_be_used:
                    curr = can_be_used.pop()
                    ans += freq - curr
                    freq_count[freq] -= 1
                else:
                    ans += (freq_count[freq]-1)*freq
                    freq_count[freq] = 0
        return ans