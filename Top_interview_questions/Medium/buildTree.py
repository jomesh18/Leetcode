'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

8271

220

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
Accepted
693,897
Submissions
1,205,619
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder: return None

            root = TreeNode(preorder[0])
            pos = inorder.index(preorder[0])

            left_in = inorder[:pos]
            right_in = inorder[pos+1:]

            left_pre = preorder[1: pos+1]
            right_pre = preorder[pos+1:]

            root.left = self.buildTree(left_pre, left_in)
            root.right = self.buildTree(right_pre, right_in)
            
            return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {v: i for i, v in enumerate(inorder)}
        
        def build(pre_beg, pre_end, in_beg, in_end):
            if pre_beg > pre_end: return None
            root_ind = d[preorder[pre_beg]]
            root = TreeNode(inorder[root_ind])
            root.left = build(pre_beg+1, pre_beg+root_ind-in_beg, in_beg, root_ind-1)
            root.right = build(pre_beg+root_ind-in_beg+1,  pre_end, root_ind+1, in_end)
            return root
    
        return build(0, len(preorder)-1, 0, len(inorder)-1)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)