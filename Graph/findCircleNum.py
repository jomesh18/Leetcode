# '''
# Number of Provinces

# Solution
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# '''
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         size = len(isConnected)
        
#         class UnionFind:
#             def __init__(self, size):
#                 self.root = [i for i in range(size)]
#                 self.rank = [1]*size
            
#             def find(self, x):
#                 if self.root[x] == x:
#                     return x
#                 self.root[x] = self.find(self.root[x])
#                 return self.root[x]
            
#             def union(self, x, y):
#                 rootX = self.find(x)
#                 rootY = self.find(y)
                
#                 if rootX != rootY:
#                     if self.rank[rootX] > self.rank[rootY]:
#                         self.root[rootY] = rootX
#                     elif self.rank[rootX] < self.rank[rootY]:
#                         self.root[rootX] = rootY
#                     else:
#                         self.root[rootY] = rootX
#                         self.rank[rootX] += 1
            
#             def connected(self, x, y):
#                 return self.find(x) == self.find(y)
            
#         UF = UnionFind(size)
        
#         for i in range(size):
#             for j in range(size):
#                 if isConnected[i][j] == 1:
#                     UF.union(i, j)
        
#         provinces = set()
        
#         for i in range(size):
#             provinces.add(UF.find(i))
            
#         return len(provinces)


# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.count = size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        return uf.getCount()