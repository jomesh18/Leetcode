'''
99. Recover Binary Search Tree
Medium

4585

159

Add to List

Share
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
Accepted
294,002
Submissions
623,586
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#O(n), O(h)
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        correct_order = None
        def dfs(node):
            if node:
                dfs(node.left)
                if correct_order:
                    if node.val != correct_order[-1]:
                        node.val = correct_order[-1]
                    correct_order.pop()
                res.append(node.val)
                dfs(node.right)

        dfs(root)
        res.sort(reverse=True)
        correct_order = res[:]
        res = []
        dfs(root)

#O(n), O(1) space
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first_elem, self.second_elem, self.prev_elem = None, None, TreeNode(float("-inf"))
        
        def dfs(node):
            if node:
                dfs(node.left)
                if self.first_elem is None and self.prev_elem.val > node.val:
                    self.first_elem = self.prev_elem
                if self.first_elem is not None and self.prev_elem.val > node.val:
                    self.second_elem = node
                self.prev_elem = node
                dfs(node.right)
        dfs(root)
        # print(self.first_elem)
        # print(self.second_elem)
        # print(self.prev_elem)
        self.first_elem.val, self.second_elem.val = self.second_elem.val, self.first_elem.val
        
