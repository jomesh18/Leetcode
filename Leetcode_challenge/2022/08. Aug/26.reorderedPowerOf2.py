'''
869. Reordered Power of 2
Medium

1025

264

Add to List

Share
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
Accepted
59,456
Submissions
94,934
'''
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_set = [Counter(str(1<<i)) for i in range(32)]
        return Counter(str(n)) in power_set

