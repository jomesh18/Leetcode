'''
450. Delete Node in a BST
Medium

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

 

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -105 <= Node.val <= 105
    Each node has a unique value.
    root is a valid binary search tree.
    -105 <= key <= 105

 

Follow up: Could you solve it with time complexity O(height of tree)?
Accepted
220,183
Submissions
463,037
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#accepted, iterative my try
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(float("inf"), root, None)
        def searchNode(node, prev, prevIsLeft):
            if not node: return (None, None, None)
            if node.val < key:
                return searchNode(node.right, node, False)
            elif node.val > key:
                return searchNode(node.left, node, True)
            else:
                return (node, prev, prevIsLeft)
        node, prev, prevIsLeft = searchNode(root, dummy, True)
        # node not found
        if not node: return root
        # node is child node
        if not node.left and not node.right:
            if prevIsLeft: prev.left = None
            else: prev.right = None
            return dummy.left
        # node has no right child
        elif not node.right:
            if prevIsLeft: prev.left = node.left
            else: prev.right = node.left
            return dummy.left
        # node has right child
        else:
            node = node.right
            old = None
            while node.left:
                old = node
                node = node.left
            if old: old.left = node.right
            if prevIsLeft:
                node.left = prev.left.left
                if node != prev.left.right:
                    node.right = prev.left.right
                prev.left = node
            else:
                node.left = prev.right.left
                if node != prev.right.right:
                    node.right = prev.right.right
                prev.right = node
            return dummy.left

#from leetcode
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right: return root.left
            elif not root.left: return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        return root