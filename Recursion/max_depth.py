'''
  Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Example 3:

Input: root = []
Output: 0

Example 4:

Input: root = [0]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if not root: return 0
        def helper(root, count):
            if not root: return count
            count += 1
            return max(helper(root.left, count), helper(root.right, count))
        return helper(root, 0)

#from leetcode one liner
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        
def build_tree(root):
    if not root: return root
    start = TreeNode(root[0])
    i = 1
    q = [start]
    while i<len(root):
        curr = q.pop(0)
        if root[i] is not None:
            curr.left = TreeNode(root[i])
            q.append(curr.left)
        i += 1
        if root[i] is not None:
            curr.right = TreeNode(root[i])
            q.append(curr.right)
        i += 1
    return start

def print_tree(root):
    ans = []
    q = [root]
    while q:
        curr = q.pop(0)
        if curr:
            ans.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        else:
            ans.append(None)
    return ans

root = [3,9,20,None,None,15,7]
# Output: 3
start = build_tree(root)
print(print_tree(start))
s = Solution()
print(s.maxDepth(start))
