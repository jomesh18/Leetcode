'''
1382. Balance a Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []
        vals = dfs(root)
        def make_bst(arr, l, r):
            if l > r:
                return None
            elif l == r:
                return TreeNode(arr[l])
            m = (l + r) // 2
            node = TreeNode(arr[m])
            node.left = make_bst(arr, l, m-1)
            node.right = make_bst(arr, m+1, r)
            return node
        
        return make_bst(vals, 0, len(vals)-1)
