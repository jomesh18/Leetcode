'''
386. Lexicographical Numbers
Medium

2272

166

Add to List

Share
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def helper(num):
            if num > n:
                return
            else:
                ans.append(num)
            num_mul_10 = num * 10
            for i in range(10):
                if (num_mul_10 + i) > n:
                    break
                if (num_mul_10 + i) == 0:
                    continue
                helper(num_mul_10+i)
            return ans
        helper(0)
        return ans[1:]