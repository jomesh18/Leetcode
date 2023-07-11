'''
863. All Nodes Distance K in Binary Tree
Medium

9119

176

Add to List

Share
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)
        
        def dfs(node, parent):
            if node and parent:
                g[parent.val].append(node.val)
                g[node.val].append(parent.val)
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        dfs(root, None)
        
        q = [target.val]
        visited = {target.val}
        level = 0
        while q:
            nq = []
            if level == k: return q
            for i in q:
                for j in g[i]:
                    if j not in visited:
                        visited.add(j)
                        nq.append(j)
            level += 1
            q = nq
        return []