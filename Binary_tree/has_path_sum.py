'''
Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:

Input: root = [1,2], targetSum = 0
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000


'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#iterative, bfs using queue
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root: return False

#         q = deque([root])
#         s = deque([root.val])
#         while q:
#           curr = q.popleft()
#           curr_sum = s.popleft()
#           if curr:
#               if not curr.left and not curr.right:
#                   if curr_sum == targetSum: return True
#               else:
#                   if curr.left:
#                       s.append(curr_sum + curr.left.val)
#                       q.append(curr.left)
#                   if curr.right:
#                       s.append(curr_sum + curr.right.val)
#                       q.append(curr.right)
#         return False

#dfs using stack
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#       if not root: return False
#       stack = [(root, root.val)]
#       while stack:
#           curr, curr_sum = stack.pop()
#           if not curr.left and not curr.right and curr_sum == targetSum: 
#               return True
#           else:
#               if curr.right:
#                   stack.append((curr.right, curr_sum+curr.right.val))
#               if curr.left:
#                   stack.append((curr.left, curr_sum+curr.left.val))
#       return False

#recursive, my own
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root: return False
#         return True if self.dfs(root, root.val, targetSum) else False

#     def dfs(self, curr, curr_sum, targetSum):
#         if curr: print(curr.val)
#         if not curr.left and not curr.right and curr_sum == targetSum: 
#             return True
#         else:
#             if curr.right:
#                 if self.dfs(curr.right, curr_sum+curr.right.val, targetSum):
#                     return True
#             if curr.left:
#                 if self.dfs(curr.left, curr_sum+curr.left.val, targetSum):
#                     return True
#recursive, less lines of above
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root: return False
#         def dfs(curr, curr_sum, targetSum):
#             if not curr.left and not curr.right and curr_sum == targetSum: return True
#             else:
#                 if curr.right and dfs(curr.right, curr_sum+curr.right.val, targetSum): return True
#                 if curr.left and dfs(curr.left, curr_sum+curr.left.val, targetSum): return True
#         return True if dfs(root, root.val, targetSum) else False

#from leetcode, oldcoding farmer, recursive
def hasPathSum1(self, root, sum):
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
 
#from leetcode, oldcoding farmer, DFS + stack   
def hasPathSum(self, root, sum):
    stack = [(root, sum)]
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right and node.val == value:
                return True
            stack.append((node.right, value-node.val))
            stack.append((node.left, value-node.val))
    return False        
    
def create_tree(root):
    if not root:
        return
    start = TreeNode(root.pop(0))
    q = deque([start])
    while root:
        curr = q.popleft()
        if curr:
            l = root.pop(0)
            r = root.pop(0) if root else None
            curr.left = TreeNode(l) if l else None
            curr.right = TreeNode(r) if r else None
            q.extend([curr.left, curr.right])
    return start

def print_level_order(root):
    if not root: return None
    level = [root]
    ans = []
    while any(level):
        ans.append([i.val if i else None for i in level])
        level = [i for n in level if n for i in (n.left, n.right)]
    return ans

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
# Output: true
start = create_tree(root)
# print(print_level_order(start))
s = Solution()
print(s.hasPathSum(start, targetSum))
