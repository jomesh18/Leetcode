'''
767. Reorganize String
Medium

6974

215

Add to List

Share
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-val, key) for key, val in count.items()]
        heapify(heap)
        ans = []
        while heap:
            v1, k1 = heappop(heap)
            if not ans or ans[-1] != k1:
                ans.append(k1)
                if -v1 > 1:
                    heappush(heap, (v1+1, k1))
                continue
            else:
                if not heap:
                    return ''
                v2, k2 = heappop(heap)
                ans.append(k2)
                if -v2 > 1:
                    heappush(heap, (v2+1, k2))
                heappush(heap, (v1, k1))
        return ''.join(ans)