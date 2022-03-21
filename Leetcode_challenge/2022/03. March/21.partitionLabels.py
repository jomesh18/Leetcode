'''
763. Partition Labels
Medium

6906

262

Add to List

Share
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
Accepted
350,579
Submissions
443,142
'''
#O(n)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i
        res = []
        start = 0
        i = 0
        end = 0
        for i in range(len(s)):
            if last[s[i]] > end:
                end = last[s[i]]
            elif i == end:
                # print(i, res, start, end)
                res.append(end-start+1)
                start = i + 1
                end = start
        return res

#O(n) more compact than above
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        start, end, res = 0, 0, []
        for i, c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                res.append(end-start+1)
                start = i + 1
        return res