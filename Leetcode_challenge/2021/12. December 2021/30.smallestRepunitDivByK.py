'''
1015. Smallest Integer Divisible by K
Medium

562

540

Add to List

Share
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
 

Constraints:

1 <= k <= 105
Accepted
35,153
Submissions
80,152
Seen this question in a real interview before?

Yes

No
'''

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 1
        n_len = 1
        for _ in range(k):
            if remainder % k == 0:
                return n_len
            remainder = remainder * 10 + 1
            remainder %= k
            n_len += 1
        return -1


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for n_len in range(1, k-1):
            remainder = (remainder * 10 + 1)%k
            if remainder % k == 0: return n_len
        return -1