'''
Smallest String With Swaps
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
'''
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        size = len(s)
        
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(26)]
                self.rank = [ord(s[i]) for i in range(size)]
            
            def find(self, x):
                if self.root[x] == x:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                
                if rootX != rootY:
                    if self.rank[rootX] < self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX] > self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1

            def connected(self, x, y):
                return self.find(x) == self.find(y)
            
        UF = UnionFind(size)
        
        for pair in pairs:
            UF.union(*pair)
        
        res = []
        for c in s:
            res.append(UF.find(c))
            
        return "".join(res)
