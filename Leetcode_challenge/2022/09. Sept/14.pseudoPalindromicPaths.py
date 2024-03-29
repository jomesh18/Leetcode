'''
1457. Pseudo-Palindromic Paths in a Binary Tree
Medium

1268

46

Add to List

Share
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 9
Accepted
62,723
Submissions
93,109
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def is_palin(arr):
            return len([1 for val in arr if val%2]) <= 1
        
        self.count = 0
        def dfs(node, d):
            if not node: return
            d[node.val] = d.get(node.val, 0) + 1
            if not node.left and not node.right:
                if is_palin(list(d.values())):
                    self.count += 1
            else:
                dfs(node.left, d)
                dfs(node.right, d)
            d[node.val] -= 1
        
        dfs(root, {})
        return self.count

#using mask and xor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(node, path):
            if not node: return
            path ^= (1<<node.val)
            if not node.left and not node.right:
                if not path & (path-1): self.count += 1
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path ^= (1<<node.val)
        
        dfs(root, 0)
        return self.count
    