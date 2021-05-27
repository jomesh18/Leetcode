'''
Clone Graph

Solution
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Example 4:


Input: adjList = [[2],[1]]
Output: [[2],[1]]
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
'''

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

#recursive, my try
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node: return node
#         visited = []
#         new_nodes = {node.val: Node(node.val)}

#         def dfs(node):
#             if node in visited: return
#             visited.append(node)
#             for n in node.neighbors:
#                 if n.val not in new_nodes:
#                     new_nodes[n.val] = Node(n.val)
#                 new_nodes[node.val].neighbors.append(new_nodes[n.val])
#                 dfs(n)
#         dfs(node)
#         return new_nodes[node.val]          

# recursive, from leetcode, old coding farmer
    def cloneGraph(self, node): # DFS recursively
        if not node:
            return node
        m = {node: Node(node.val)}
        self.dfs(node, m)
        return m[node]

    def dfs(self, node, m):
        for neigh in node.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
                self.dfs(neigh, m)
            m[node].neighbors.append(m[neigh])

# recursive, concise, from dbabichev

class Solution:
    def cloneGraph(self, node):
        def dfs(node):
            mapping[node] = Node(node.val)
            for neigh in node.neighbors:
                if neigh not in mapping: dfs(neigh)
                mapping[node].neighbors += [mapping[neigh]]
        
        if not node: return node
        mapping  = {}
        dfs(node)
        return mapping[node]


#using stack dfs, my try
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        stack = [node]
        visited = {}
        new_nodes = {node.val: Node(node.val)}
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited[current_node] = True
                for n in current_node.neighbors:
                    if n.val not in new_nodes:
                        new_nodes[n.val] = Node(n.val)
                    new_nodes[current_node.val].neighbors.append(new_nodes[n.val])
                    if n not in visited:
                        stack.append(n)
        return new_nodes[node.val]

# dfs from leetcode, old coding farmer

class Solution(object):
    def cloneGraph1(self, node): #DFS iteratively
        if not node:
            return node
        m = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in m:
                    stack.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
        return m[node]

def create_graph(adjList):
    created_nodes = [None] * len(adjList)
    for ind, lis in enumerate(adjList):
        if created_nodes[ind]:
            current_node = created_nodes[ind]
        else:
            current_node = Node(ind+1)
            created_nodes[ind] = current_node
        for val in lis:
            if created_nodes[val-1] is None:
                created_nodes[val-1] = Node(val)
            current_node.neighbors.append(created_nodes[val-1])
    return created_nodes[0]

def print_graph(node):
    visited = []
    def dfs(node):
        if node in visited:
            return
        visited.append(node)
        for n in node.neighbors:
            dfs(n)
    dfs(node)
    print([n.val for n in visited])
    adj_list = [None] * len(visited)
    for n in visited:
        adj_list[n.val-1] = n.neighbors
    res = []
    for l in adj_list:
        res.append([n.val for n in l])
    print(res)


adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
start = create_graph(adjList)
print_graph(start)
s = Solution()
cloned_graph_start = s.cloneGraph(start)
print_graph(cloned_graph_start)
