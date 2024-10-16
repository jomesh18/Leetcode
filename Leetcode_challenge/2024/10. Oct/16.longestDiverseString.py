'''
1405. Longest Happy String
Medium

2199

268

Add to List

Share
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
#         max_ = max(a, b, c)
#         tot = a + b + c
#         res_len = min(tot, 2 + 3 * (tot-max_))
        
        ans = []
        pq = []
        if a:
            pq.append((-a, 'a'))
        if b:
            heappush(pq, (-b, 'b'))
        if c:
            heappush(pq, (-c, 'c'))
        while len(pq) > 1:
            count, c = heappop(pq)
            if not ans or (ans and ans[-1] != c):
                for _ in range(min(2, -count)):
                    ans.append(c)
                count += 2
            count2, c2 = heappop(pq)
            ans.append(c2)
            count2 += 1
            if count < 0:
                heappush(pq, (count, c))
            if count2 < 0:
                heappush(pq, (count2, c2))
        if pq and (not ans or pq[0][1] != ans[-1]):
            ans.append(pq[0][1])
            if -pq[0][0] > 1:
                ans.append(pq[0][1])
        return ''.join(ans)