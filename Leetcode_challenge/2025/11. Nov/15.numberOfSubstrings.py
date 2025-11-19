'''
3234. Count the Number of Substrings With Dominant Ones
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

Example 1:

Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.

i	j	s[i..j]	Number of Zeros	Number of Ones
3	3	1	0	1
4	4	1	0	1
2	3	01	1	1
3	4	11	0	2
2	4	011	1	2
Example 2:

Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3
 

Constraints:

1 <= s.length <= 4 * 104
s consists only of characters '0' and '1'.
'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for k in range(1, int(n**.5)+1):
            ones = 0
            q = deque([])
            last_ind = -1
            for i in range(n):
                if s[i] == '0':
                    q.append(i)
                    if len(q) > k:
                        ones -= q[0] - last_ind - 1
                        last_ind = q.popleft()
                else:
                    ones += 1
                if len(q) == k and ones >= k*k:
                    ans += min(q[0]-last_ind, ones-k*k+1)

        cons = 0
        for i in range(n):
            if s[i] == '0':
                ans += (cons * (cons+1)//2)
                cons = 0
            else:
                cons += 1
        ans += cons * (cons+1)//2
        
        return ans
