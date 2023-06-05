'''
547. Number of Provinces
Medium

8240

311

Add to List

Share
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
        provinces = 0
        n = len(isConnected)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    g[i].append(j)
                    g[j].append(i)
        
        visited = [False]*n
        def dfs(i):
            visited[i] = True
            for nei in g[i]:
                if not visited[nei]:
                    dfs(nei)
                    
        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1
        return provinces
    