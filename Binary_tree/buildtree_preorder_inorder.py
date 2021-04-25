'''
Construct Binary Tree from Preorder and Inorder Traversal

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

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def buildTree(self, preorder: [], inorder: []) -> TreeNode:
#       if not inorder: return None
#       ind = inorder.index(preorder.pop(0))
#       root = TreeNode(inorder[ind])
#       root.left = self.buildTree(preorder[:ind], inorder[:ind])
#       root.right = self.buildTree(preorder[ind:], inorder[ind+1:])
#       return root

# class Solution:
#     def buildTree(self, preorder: [], inorder: []) -> TreeNode:
#       if inorder:
#           ind = inorder.index(preorder.pop(0))
#           root = TreeNode(inorder[ind])
#           root.left = self.buildTree(preorder, inorder[:ind])
#           root.right = self.buildTree(preorder, inorder[ind+1:])
#           return root
        
# class Solution:
#     def buildTree(self, preorder: [], inorder: []) -> TreeNode:
#         dict = {value: ind for ind, value in enumerate(inorder)}
#         def build(pre_beg, pre_end, in_beg, in_end):
#             if in_end<=in_beg: return None
#             ind = dict[preorder[pre_beg]]
#             root = TreeNode(inorder[ind])
#             root.left = build(pre_beg+1, pre_beg+ind-in_beg+1, in_beg, ind)
#             root.right = build(pre_end-in_end+ind+1, pre_end, ind+1, in_end)
#             return root
#         return build(0, len(preorder), 0, len(inorder))

#from leetcode solution
class Solution:
    def buildTree(self, preorder: [], inorder: []) -> TreeNode:

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

#from leetcode 
'''Consider this input:

preorder: [1, 2, 4, 5, 3, 6]
inorder: [4, 2, 5, 1, 6, 3]
The obvious way to build the tree is:

Use the first element of preorder, the 1, as root.
Search it in inorder.
Split inorder by it, here into [4, 2, 5] and [6, 3].
Split the rest of preorder into two parts as large as the inorder parts, here into [2, 4, 5] and [3, 6].
Use preorder = [2, 4, 5] and inorder = [4, 2, 5] to add the left subtree.
Use preorder =[3, 6]andinorder = [6, 3] to add the right subtree.
But consider the worst case for this: A tree that's not balanced but is just a straight line to the left. Then inorder is the reverse of preorder, and already the cost of step 2, searching in inorder, is O(n^2) overall. Also, depending on how you "split" the arrays, you're looking at O(n^2) runtime and possibly O(n^2) space for that as well.

You can bring the runtime for searching down to O(n) by building a map from value to index before you start the main work, and I've seen several solutions do that. But that is O(n) additional space, and also the splitting problems remain. To fix those, you can use pointers into preorder and inorder instead of splitting them. And when you're doing that, you don't need the value-to-index map, either.

Consider the example again. Instead of finding the 1 in inorder, splitting the arrays into parts and recursing on them, just recurse on the full remaining arrays and stop when you come across the 1 in inorder. That's what my above solution does. Each recursive call gets told where to stop, and it tells its subcalls where to stop. It gives its own root value as stopper to its left subcall and its parent`s stopper as stopper to its right subcall.
'''
class Solution
    def buildTree(self, preorder, inorder):
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)

def print_tree(ans):
    q = [ans]
    res = []
    while any(q):
        curr = q.pop(0)
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else: res.append(None)
    return res

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
s = Solution()
ans = s.buildTree(preorder, inorder)
print(print_tree(ans))
        