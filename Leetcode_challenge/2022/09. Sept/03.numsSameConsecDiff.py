'''
967. Numbers With Same Consecutive Differences
Medium

2489

183

Add to List

Share
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Constraints:

2 <= n <= 9
0 <= k <= 9
Accepted
109,832
Submissions
193,120
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if k == 0:
            return [int(str(i)*n) for i in range(1, 10)]
        g = defaultdict(list)
        for i in range(10):
            if len(str(i+k)) == 2:
                break
            g[str(i)].append(str(i+k))
            g[str(i+k)].append(str(i))
        # print(g)
        def backtrack(node, path):
            if len(path) == n:
                self.res.append(int(''.join(path)))
                return
            for nex in g[node]:
                backtrack(nex, path+[nex])
        
        self.res = []
        for key in g:
            if key != '0':
                backtrack(key, [key])
        return self.res


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # if k == 0:
        #     return [int(str(i)*n) for i in range(1, 10)]
        g = defaultdict(list)
        for i in range(10):
            if len(str(i+k)) == 2:
                break
            g[str(i)].append(str(i+k))
            if k != 0:
                g[str(i+k)].append(str(i))
        # print(g)
        def backtrack(node, path):
            if len(path) == n:
                self.res.append(int(''.join(path)))
                return
            for nex in g[node]:
                backtrack(nex, path+[nex])
        
        self.res = []
        for key in g:
            if key != '0':
                backtrack(key, [key])
        return self.res