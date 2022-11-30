'''
Binary Tree Maximum Path Sum

Solution
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            if not curr: return (float('-inf'), float('-inf'))
            left_using, left_not_using = dfs(curr.left)
            right_using, right_not_using = dfs(curr.right)
            using = max(left_using+curr.val, right_using + curr.val, curr.val)
            not_using = max(left_not_using, right_not_using, left_using, right_using, curr.val+left_using+right_using)
            return (using, not_using)
        
        return max(dfs(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(curr):
            nonlocal ans
            if not curr: return 0
            left = max(dfs(curr.left), 0)
            right = max(dfs(curr.right), 0)
            ans = max(left+right+curr.val, ans)
            return max(curr.val+left, curr.val+right)
            
        dfs(root)
        return ans

