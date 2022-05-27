'''
1192. Critical Connections in a Network
Hard

4476

162

Add to List

Share
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
Accepted
173,884
Submissions
320,519
'''
# link for this algo
# https://www.geeksforgeeks.org/bridge-in-a-graph/
# tarson's algorithm
'''
    def bridgeUtil(self,u, visited, parent, low, disc):
 
        # Mark the current node as visited and print it
        visited[u]= True
 
        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
 
        #Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False :
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc)
 
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])
 
 
                ''' If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge'''
                if low[v] > disc[u]:
                    print ("%d %d" %(u,v))
     
                     
            elif v != parent[u]: # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[v])
                '''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        
        for s, d in connections:
            g[s].append(d)
            g[d].append(s)
            
        parent = [-2]*n
        visited = [0]*n
        low = [-1]*n
        disc = [-1]*n
        res = []
        self.time = 0
        
        def dfs(u):
            visited[u] = 1
            disc[u] = self.time
            low[u] = self.time
            self.time += 1
            
            for v in g[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)
                    if low[v] < low[u]:
                        low[u] = low[v]
                    if low[v] > disc[u]:
                        res.append([u, v])
                elif parent[u] != v:
                    low[u] = min(disc[v], low[u])
                    
        dfs(0)
        return res