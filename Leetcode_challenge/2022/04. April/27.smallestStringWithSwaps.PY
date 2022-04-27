'''
1202. Smallest String With Swaps
Medium

2170

67

Add to List

Share
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
Accepted
60.8K
Submissions
110.2K
'''
#USING UNION FIND
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(s)
        class UF:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [0]*size
            
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px != py:
                    if self.rank[px] > self.rank[py]:
                        self.root[py] = px
                    elif self.rank[py] > self.rank[px]:
                        self.root[px] = py
                    else:
                        self.root[py] = px
                        self.rank[px] += 1
            
            def connected(self, x, y):
                return self.find(x) == self.find(y)
            
        uf = UF(size)
        for u, v in pairs:
            uf.union(u, v)
        
        d = defaultdict(list)
        for i in range(size):
            root = uf.find(i)
            d[root].append(s[i])
        
        for key in d:
            d[key] = sorted(d[key], reverse=True)
        
        new = []
        for i in range(size):
            group = uf.find(i)
            new.append(d[group].pop())
        return "".join(new)
    
#dfs
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        def dfs(i):
            visited[i] = True
            connected.append(i)
            for j in adj_list[i]:
                if not visited[j]:
                    dfs(j)
            
        adj_list = [[] for _ in range(n)]
        for u, v in pairs:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False]*n
        new = [None]*n
        for i in range(n):
            if not visited[i]:
                connected = []
                dfs(i)
                connected.sort()
                chars = [s[i] for i in connected]
                chars.sort()
                for i in range(len(connected)):
                    new[connected[i]] = chars[i]
        return "".join(new)
