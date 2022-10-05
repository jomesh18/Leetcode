'''
623. Add One Row to Tree
Medium

1762

197

Add to List

Share
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
 

Example 1:


Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]
Example 2:


Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
The depth of the tree is in the range [1, 104].
-100 <= Node.val <= 100
-105 <= val <= 105
1 <= depth <= the depth of tree + 1
'''
#bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        level = 1
        q = [root]
        while level < depth-1:
            level += 1
            new_q = []
            for curr in q:
                if curr.left: new_q.append(curr.left)
                if curr.right: new_q.append(curr.right)
            q = new_q
        
        for node in q:
            new_node = TreeNode(val)
            new_node.left = node.left
            node.left = new_node
            new_node = TreeNode(val)
            new_node.right = node.right
            node.right = new_node
        return root

#dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, d):
            if not node: return
            if d == depth-1:
                new_node = TreeNode(val)
                new_node.left = node.left
                node.left = new_node
                new_node = TreeNode(val)
                new_node.right = node.right
                node.right = new_node
            else:
                dfs(node.left, d+1)
                dfs(node.right, d+1)
            return node
                
        if depth == 1:
            return TreeNode(val, root, None)
        else:
            return dfs(root, 1)