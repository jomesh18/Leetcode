'''
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.

'''
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         res = []
#         found = 0
#         def find(root, path):
#             nonlocal res, p, q, found
#             if found == 2:
#                 return
#             if not root:
#                 return
#             path.append(root)
#             if root.val == p.val or root.val == q.val:
#                 # ans = [i.val for i in path]
#                 # res.append(ans)
#                 res.append(path[:])
#                 found += 1
            
#             if not root.right and not root.left:
#                 path.remove(root)
#                 return

#             find(root.left, path)
#             find(root.right, path)
#             path.remove(root)

#         find(root, [])
#         # print(res)
#         ans = None
#         for u, v in zip(res[0], res[1]):
#             if u != v:
#                 break
#             ans = u
#         return ans

#from leetcode solution, my try, recursive
# class Solution:
#     def __init__(self):
#         # variable to store the lca node
#         self.ans = None

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         def recurse_tree(current_node):
#             # if reached the end of the branch, return False.
#             if not current_node: return False
#             # left traversal
#             left = recurse_tree(current_node.left)
#             # right traversal
#             right = recurse_tree(current_node.right)
#             # if current node is one of p or q
#             mid = (current_node == p or current_node == q)
#             # if any two of left, right, mid is true, we found the lca
#             if mid+left+right >= 2:
#                 self.ans = current_node
#             # return True if any is found
#             return mid or left or right
#         recurse_tree(root)
#         return self.ans

#from leetcode solution, my try, iterative with parent pointers
# class Solution:

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # stack for tree traversal
#         stack = [root]
#         # dictionary for parent pointers
#         parent = {root: None}
#         # Iterate until we find both the nodes p and q
#         while p not in parent or q not in parent:

#             curr = stack.pop()
#             # While traversing the tree, keep saving the parent pointers.
#             if curr.right:
#                 parent[curr.right] = curr
#                 stack.append(curr.right)
#             if curr.left: 
#                 parent[curr.left] = curr
#                 stack.append(curr.left)

#         # Ancestors set() for node p.
#         ancestors = set()

#         # Process all ancestors for node p using parent pointers.
#         while p:
#             ancestors.add(p)
#             p = parent[p]

#         # The first ancestor of q which appears in
#         # p's ancestor set() is their lowest common ancestor.
#         while q not in ancestors:
#             q = parent[q]
#         return q

#from leetcode solution, iterative without parent pointers
class Solution:

    # Three static flags to keep track of post-order traversal.

    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Initialize the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]

        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != Solution.BOTH_DONE:

                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None

#from leetcode
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right

#from leetcode, same as above, but with explanation
def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
                # If looking for me, return myself
        if root == p or root == q:
            return root
        
        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way, 
        # because in such scenarios, node where 'p' found is LCA
            return left or right

def build_tree(root):
    start = TreeNode(root[0])
    q = [start]
    i = 1
    while i<len(root):
        curr = q.pop(0)
        if curr:
            if root[i] is not None: curr.left = TreeNode(root[i])
            i += 1
            if i >= len(root): break
            if root[i] is not None: curr.right = TreeNode(root[i])
            q.extend([curr.left, curr.right])
        i += 1
    return start

def print_tree(root):
    res = []
    q = [root]
    while any(q):
        curr = q.pop(0)
        if curr:
            res.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        else:
            res.append(None)
    return res

def find_node(root, val):
    if not root: return
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

# root = [3,5,1,6,2,0,8,None,None,7,4]
# p = 5
# q = 1
# Output: 3
root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 4
# # Output: 5
# root = [1,2]
# p = 1
# q = 2
# Output: 1
start = build_tree(root)
print(print_tree(start))
s = Solution()
p = find_node(start, p)
# print(p.val)
q = find_node(start, q)
# print(q.val)
print(s.lowestCommonAncestor(start, p, q).val)
