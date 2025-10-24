'''
2048. Next Greater Numerically Balanced Number
Solved
Medium
Topics
premium lock icon
Companies
Hint
An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 106
'''
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        cands = sorted([1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 41444, 44144, 44414, 44441, 22333, 23233, 23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 55555, 122333, 123233, 123323, 123332, 132233, 132323, 132332, 133223, 133232, 133322, 212333, 213233, 213323, 213332, 312233, 312323, 312332, 313223, 313232, 313322, 221333, 231233, 231323, 231332, 321233, 321323, 321332, 331223, 331232, 331322, 223133, 232133, 233123, 233132, 322133, 323123, 323132, 332123, 332132, 333122, 223313, 232313, 233213, 233312, 322313, 323213, 323312, 332213, 332312, 333212, 223331, 232331, 233231, 233321, 322331, 323231, 323321, 332231, 332321, 333221, 155555, 515555, 551555, 555155, 555515, 555551, 666666, 224444, 242444, 244244, 244424, 244442, 422444, 424244, 424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 1224444])

        i = bisect_right(cands, n)
        # print(len(set(cands)))
        # print(cands)
        # print(i)
        return cands[i]
