'''
104. Maximum Depth of Binary Tree
Easy

6271

118

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
Accepted
1,523,558
Submissions
2,136,145
Seen this question in a real interview before?

Yes

No
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ans, curr):
            if not node: return max(ans, curr)
            left = dfs(node.left, ans, curr+1)
            right = dfs(node.right, ans, curr+1)
            return max(left, right)
            
        return dfs(root, 0, 0)