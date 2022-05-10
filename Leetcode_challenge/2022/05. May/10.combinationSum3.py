'''
216. Combination Sum III
Medium

3132

76

Add to List

Share
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
Accepted
303,312
Submissions
467,859
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, temp):
            if len(temp) == k and sum(temp) == n:
                res.append(temp[:])
                return
            for j in range(i+1, 10):
                backtrack(j, temp+[j])
        backtrack(0, [])
        
        print(res)
        return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(n, k, temp):
            if n < 0 or k < 0: return
            if n == 0 and k == 0:
                res.append(temp[:])
                return
            start = temp[-1]+1 if temp else 1
            for j in range(start, 10):
                backtrack(n-j, k-1, temp+[j])
        backtrack(n, k, [])
        
        print(res)
        return res