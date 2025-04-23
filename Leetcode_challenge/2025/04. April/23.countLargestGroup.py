'''
1399. Count Largest Group
Solved
Easy
Topics
Companies
Hint
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104

'''
class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter()
        def digit_sum(i):
            s = 0
            while i:
                s += i % 10
                i //= 10
            return s

        max_count = 0
        for i in range(1, n+1):
            s = digit_sum(i)
            count[s] = count.get(s, 0) + 1
            max_count = max(count[s], max_count)
        
        return sum(1 for val in count.values() if val == max_count)
        