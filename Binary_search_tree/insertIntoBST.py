'''
Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

 

Constraints:

    The number of nodes in the tree will be in the range [0, 104].
    -108 <= Node.val <= 108
    All the values Node.val are unique.
    -108 <= val <= 108
    It's guaranteed that val does not exist in the original BST.

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#iterative
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root: return TreeNode(val)
#         prev = None
#         curr = root
#         while curr:
#             prev = curr
#             if val > curr.val:
#                 curr = curr.right
#             else:
#                 curr = curr.left
#         if val>prev.val:
#             prev.right = TreeNode(val)
#         else:
#             prev.left = TreeNode(val)
#         return root

#recursive
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root: return TreeNode(val)
#         def helper(curr, prev):
#             if not curr:
#                 return prev
#             if val > curr.val:
#                 return helper(curr.right, curr)
#             else:
#                 return helper(curr.left, curr)

#         prev = helper(root, None)
#         # print(prev.val)
#         if val>prev.val:
#             prev.right = TreeNode(val)
#         else:
#             prev.left = TreeNode(val)
#         return root

#recursive, from leetcode
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root

#recursive another one from leetcode
# class Solution:
#     def insertIntoBST(self, root, val):
#         def dfs(root):
#             if val < root.val:
#                 if root.left:
#                     dfs(root.left)
#                 else:
#                     root.left = TreeNode(val)
#             else:
#                 if root.right:
#                     dfs(root.right)
#                 else:
#                     root.right = TreeNode(val)
        
#         if not root: return TreeNode(val)
#         dfs(root)
#         return root

def build_tree(root):
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i<len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            q.append(curr.left)
            if i<len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                q.append(curr.right)
        i += 1
    return start

def print_tree(start):
    res = []
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

root = [4,2,7,1,3]
val = 5
# # # Output: [4,2,7,1,3,5]

root = [40,20,60,10,30,50,70]
val = 25
# # # Output: [40,20,60,10,30,50,70,null,null,25]

root = [4,2,7,1,3,null,null,null,null,null,null]
val = 5
# # Output: [4,2,7,1,3,5]

start = build_tree(root)
print(print_tree(start))

s = Solution()
res = s.insertIntoBST(start, val)
print(print_tree(res))
