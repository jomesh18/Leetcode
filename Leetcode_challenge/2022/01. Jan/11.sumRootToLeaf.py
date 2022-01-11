'''
1022. Sum of Root To Leaf Binary Numbers
Easy

1880

128

Add to List

Share
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
Accepted
127,642
Submissions
174,741
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#accepted
class Solution:
    def sumRootToLeaf(self, root: [TreeNode]) -> int:
        self.sum = 0
        def dfs(node, s):
            if not node: return
            if not node.left and not node.right:
                self.sum += int(s+str(node.val), 2)
                return
            if node.left: dfs(node.left, s+str(node.val))
            if node.right: dfs(node.right, s+str(node.val))
        dfs(root, "")
        return self.sum

#from leetcode
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number
                    
                preorder(r.left, curr_number)
                preorder(r.right, curr_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf

null = None

root = [0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,null,1,0,0,1,1,0,1,1,0,0,0,0,1,1,1,null,0,1,0,1,1,null,1,null,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,null,1,null,0,0,null,null,null,null,null,1,null,0,1,0,0,1,null,1,1,null,null,0,0,0,0,null,1,0,1,0,0,0,1,0,0,1,0,1,0,null,null,0,1,1,0,0,null,0,0,1,0,0,1,0,1,null,1,null,null,0,null,1,null,null,0,1,null,1,1,null,null,1,1,null,1,0,1,1,0,null,null,1,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,null,1,1,1,0,null,0,0,0,0,1,0,0,0,1,0,1,null,1,1,0,null,1,null,null,0,null,0,null,0,null,0,null,null,null,null,null,null,null,null,1,1,null,null,null,null,null,0,0,0,null,1,0,1,null,0,1,0,0,1,null,0,0,null,1,1,1,null,0,null,0,null,1,null,null,1,0,0,0,1,1,null,1,0,null,null,0,0,0,0,1,1,1,0,1,1,0,0,0,null,null,1,1,null,1,1,null,null,1,0,0,0,1,1,0,1,null,1,null,null,null,null,null,0,1,1,0,0,null,1,1,null,0,null,null,1,0,1,null,1,1,0,null,null,null,0,0,null,null,null,0,null,null,null,1,null,1,1,null,0,null,0,0,1,1,null,1,null,1,0,1,1,1,1,null,null,null,1,0,0,1,0,0,null,null,null,null,null,1,0,1,1,0,0,0,0,null,0,1,0,0,0,1,0,1,null,1,1,0,1,0,1,1,0,0,1,null,null,0,0,0,0,0,0,1,null,null,null,1,1,0,1,0,1,0,null,1,0,0,null,1,1,0,null,null,1,0,1,1,0,0,1,0,1,0,1,0,null,null,0,null,0,1,null,null,null,null,null,null,null,null,0,1,0,null,null,null,1,0,1,0,1,1,null,1,0,0,0,0,null,null,null,null,1,0,null,null,null,0,0,null,0,1,null,0,null,null,null,null,1,1,0,null,null,null,0,1,1,null,null,null,null,null,1,0,null,0,null,null,null,null,null,0,1,0,1,null,null,null,0,1,0,1,1,0,1,null,null,1,1,1,null,null,0,0,0,null,null,null,null,null,null,null,null,0,null,0,1,null,1,1,1,1,1,0,1,0,1,null,0,null,1,0,1,null,null,1,null,1,0,0,1,0,1,1,1,null,null,null,null,null,1,1,1,0,1,0,0,1,0,0,1,1,1,null,null,null,1,null,1,0,1,1,1,1,0,0,0,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,1,1,1,null,0,1,0,1,null,null,1,1,null,1,0,null,0,null,null,null,null,null,1,null,null,null,null,null,0,1,1,null,null,null,null,1,null,0,1,0,null,null,1,null,null,1,1,1,0,0,0,0,null,1,1,null,null,0,null,null,0,null,null,1,null,null,null,null,null,null,null,null,null,0,null,null,null,null,1,1,null,null,null,null,null,null,1,1,null,1,null,null,null,1,1,1,1,1,1,0,null,1,null,1,null,null,1,null,1,0,0,1,0,0,0,0,null,0,1,null,null,1,null,null,0,0,1,1,1,1,null,null,null,0,1,0,1,1,null,null,null,0,null,null,0,1,0,0,null,0,null,null,0,1,0,null,null,1,0,null,null,0,1,null,1,0,null,0,null,null,1,0,0,null,null,0,null,0,1,1,0,0,0,1,1,0,0,0,null,0,0,null,null,null,null,1,0,1,0,1,0,null,0,0,1,null,1,1,1,0,1,0,null,1,0,null,null,0,0,null,0,null,0,null,null,null,null,0,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,0,null,null,1,0,null,null,0,1,null,0,null,1,null,null,1,0,null,null,null,null,0,null,null,null,null,1,1,null,1,1,1,1,1,null,null,1,null,null,null,null,null,0,null,null,0,1,null,1,1,1,null,null,1,0,null,1,0,1,null,1,null,1,null,0,0,null,1,1,1,1,0,1,0,null,0,null,0,0,null,null,null,1,1,null,null,0,null,null,null,null,null,null,null,0,1,0,0,null,null,1,null,null,0,1,null,null,null,null,1,null,0,0,null,0,1,null,null,0,null,null,0,1,1,0,1,0,null,null,null,null,null,null,null,null,null,null,null,null,null,0,0,0,0,0,null,null,0,1,null,null,0,0,1,0,0,1,1,null,1,null,1,1,0,null,1,null,1,0,1,1,0,1,null,0,null,1,1,1,null,null,null,null,0,1,0,null,1,0,1,null,null,0,null,null,1,1,1,0,1,0,1,0,null,null,null,0,1,null,null,null,null,null,null,null,null,null,null,null,0,0,0,0,null,null,null,null,null,null,null,1,null,1,null,null,null,0,null,null,0,null,null,null,0,1,0,0,null,null,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,null,0,null,null,null,null,null,null,0,0,null,null,0,0,null,0,1,null,1,0,0,null,null,0,null,null,0,null,null,1,null,1,null,null,0,0,null,1,null,null,null,0,0,0,null,1,null,1,0,1,null,1,null,1,null,0,null,null,null,1,null,null,null,1,0,null,null,null,null,null,1,null,null,null,null,null,0,null,0,0,0,1,1,1,0,1,null,0,null,null,null,null,null,null,0,null,null,null,0,null,null,null,null,null,1,0,0,null,0,0,null,null,null,0,0,0,1,null,0,null,1,null,null,null,1,null,0,0,null,1,1,1,null,null,null,1,null,null,null,null,1,null,1,1,null,null,null,null,null,null,1,null,0,0,1,null,null,null,0,null,null,null,null,1,0,0,0,1,0,0,1,null,null,null,0,null,0,null,null,null,1,1,0,null,null,null,null,null,1,null,null,null,null,0,null,null,1,null,0,null,null,0,null,null,1,null,null,0,null,null,0,null,null,1,0,1,0,null,1,0,0,1,null,null,0,1,1,null,null,null,null,null,0,1,null,null,null,null,null,0,null,null,null,null,null,null,1,0,null,0,0,0,null,null,null,null,null,null,null,null,null,null,0,null,0,0,0,1,null,0,0,null,null,null,0,1,1,null,1,0,0,1,null,null,null,null,null,null,null,null,null,null,null,null,1,1,1,1,1,0,0,0,null,1,null,1,0,0,1,null,null,0,null,null,1,null,null,null,null,null,1,0,0,null,null,null,1,0,1,0,null,0,0,1,null,1,1,0,null,null,null,1,1,null,null,null,null,null,1,null,null,null,0,null,null,null,null,null,0,0,1,null,null,0,1,1,null,null,null,null,null,null,null,null,null,0,null,null,null,null,null,null,null,null,1,null,null,null,1,null,1,null,0,null,null,null,null,null,null,null,1,1,1,0,null,null,1,null,null,null,null,null,null,0,null,null,0,null,1,1,0,null,1,1,null,1,null,null,1,null,null,1,null,0,1,null,null,null,0,0,null,null,1,0,1,1,0,null,null,1,0,null,1,0,1,1,null,null,0,0,1,0,0,1,0,0,null,null,0,0,null,0,null,null,0,null,null,1,0,0,null,1,null,null,null,1,null,null,0,null,0,0,1,0,null,1,0,null,1,null,null,1,null,null,1,null,null,null,1,null,null,null,null,1,null,null,null,null,null,null,null,null,1,null,null,0,null,null,null,null,0,null,null,1,null,null,null,null,null,null,null,0,null,0,0,null,null,1,null,0,null,1,null,null,null,null,null,null,null,null,1,null,0,null,null,null,null,null,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,null,null,0,null,1,null,1,1,null,1,null,0,null,null,1,null,null,null,null,1,null,null,null,null,0,1,0,null,1,0,0,1,1,null,0,null,1,1,0,1,0,null,null,1,null,1,null,null,null,null,1,1,null,0,1,1,0,1,null,null,0,null,0,null,null,null,null,0,null,1,null,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,1,null,null,null,null,null,0,0,null,null,0,null,0,null,null,0,0,null,0,1,1,null,0,1,1,null,null,null,null,null,null,null,null,1,1,null,0,0,0,0,null,null,1,null,null,0,0,1,null,1,null,1,null,0,null,0,0,1,null,null,null,null,null,null,null,null,null,null,null,0,null,null,1,null,null,null,null,null,null,null,0,null,null,null,null,null,null,null,1,null,0,null,1,1,null,0,null,null,null,null,null,null,1,0,0,null,0,1,null,null,0,null,null,null,null,null,null,null,1,null,null,1,null,null,1,null,null,null,0,null,null,null,null,null,null,null,null,0,null,null,0,null,null,null,null,null,null,1,0,null,null,null,null,0,1,null,null,null,null,1,null,null,1,null,null,null,null,1,null,null,null,null,null,null,null,0]
# Output: 7354215
print(len(root))

sol = Solution()
print(sol.sumRootToLeaf(root))
