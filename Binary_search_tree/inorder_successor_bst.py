'''
285: Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
'''

# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#naive solution, O(n)
# class Solution:
#     """
#     @param: root: The root of the BST.
#     @param: p: You need find the successor node of p.
#     @return: Successor of p.
#     """
#     def inorderSuccessor(self, root, p):
#         # write your code here
#         #doing iterative inorder dfs using stack
#         stack = []
#         next_is_successor = False
#         curr = root
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             if next_is_successor:
#                 # print(curr.val)
#                 return curr
#             if curr == p:
#                 next_is_successor = True
#             curr = curr.right

# #Optimized, O(h), h is height of tree
# class Solution:
#     """
#     @param: root: The root of the BST.
#     @param: p: You need find the successor node of p.
#     @return: Successor of p.
#     """
#     '''
#         If right subtree of node is not NULL, then succ lies in right subtree. Do the following. 
#     Go to right subtree and return the node with minimum key value in the right subtree.
#     If right subtree of node is NULL, then start from the root and use search-like technique. Do the following. 
#     Travel down the tree, if a node’s data is greater than root’s data then go right side, otherwise, go to left side.
#     '''
#     def inorderSuccessor(self, root, p):
#         if not root: return None
#         if p.right:
#             return self.find_min(p.right)
#         curr = root
#         succ = None
#         while curr:
#             if curr.val < p.val:
#                 curr = curr.right
#             elif curr.val > p.val:
#                 succ = curr
#                 curr = curr.left
#             else:
#                 break
#         # print(succ.val)
#         return succ

#     def find_min(self, node):
#         curr = node
#         while curr.left:
#             curr = curr.left
#         # print(curr.val)
#         return curr

#from lintcode
# class Solution:
#     """
#     @param: root: The root of the BST.
#     @param: p: You need find the successor node of p.
#     @return: Successor of p.
#     """
#     def inorderSuccessor(self, root, p):
#         if root == None:
#             return None
#         if root.val <= p.val:
#             return self.inorderSuccessor(root.right, p)

#         left = self.inorderSuccessor(root.left, p)
#         if left != None:
#             return left
#         else:
#             return root

#from lintcode
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        # if successor: print(successor.val)
        return successor

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
                curr.right = TreeNode(root[i]) if root[i] is not None else none
                q.append(curr.right)
        i += 1
    return start

def print_tree(start):
    q = deque([start])
    res = []
    while q:
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

def find_p(start, p):
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            if curr.val == p:
                return curr
            q.extend([curr.left, curr.right])
    return -1

null = None

root = [1,null,2]
p = 1
# Output: 2

root = [2,1,3]
p = 1
# Output: 2

root = [13, 3, 14, 1, 4, None, 18, None, 2]
p = 4

start = build_tree(root)
print(print_tree(start))
p_node = find_p(start, p)

s = Solution()
print(s.inorderSuccessor(start, p_node))
