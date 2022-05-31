'''
1461. Check If a String Contains All Binary Codes of Size K
Medium

1326

75

Add to List

Share
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

Constraints:

1 <= s.length <= 5 * 105
s[i] is either '0' or '1'.
1 <= k <= 20
Accepted
71,608
Submissions
126,823
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        visited = [0]*(2**k)
        i, j = 0, k
        while j <= len(s):
            curr = s[i:j]
            if not visited[int(curr, 2)]:
                visited[(int(curr, 2))] = 1
            i += 1
            j += 1
        return all(i for i in visited)
    
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:        
        need = 1<<k
        got = set()
        for i in range(k, len(s)+1):
            curr = s[i-k:i]
            if curr not in got:
                got.add(curr)
                need -= 1
                if need == 0: return True
        return False


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:        
        need = 1<<k
        got = [False]*need
        all_one = need-1
        curr_hash = 0
        
        for i in range(len(s)):
            curr_hash = ((curr_hash<<1) & all_one) | int(s[i])
            if i >= k-1 and not got[curr_hash]:
                got[curr_hash] = True
                need -= 1
                if need == 0: return True
        return False