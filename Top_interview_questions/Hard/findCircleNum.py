'''
Friend Circles

Solution
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UF:
            def __init__(self, n):
                self.root = [i for i in range(n)]
                self.rank = [0]*n
            
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px != py:
                    if self.rank[px] < self.rank[py]:
                        self.root[px] = self.root[py]
                    else:
                        self.root[py] = self.root[px]
                        if self.rank[px] == self.rank[py]:
                            self.rank[px] += 1
                
        n = len(isConnected)
        uf = UF(n) 
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
                    print(i, j, uf.root)
        s = set()
        for i in range(n):
            s.add(uf.find(i))
        return len(s)