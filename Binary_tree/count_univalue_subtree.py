'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example: Given binary tree,

              5
             / \
            1   5
           / \   \
          5   5   5

return 4.
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def univalue(self, root):
		count = [0]
		def count_univalue(root, count):
			if not root: return True
			left_ans = count_univalue(root.left, count)
			right_ans = count_univalue(root.right, count)
			if not left_ans or not right_ans: return False
			if root.left and root.val != root.left.val: return False
			if root.right and root.val != root.right.val: return False
			count[0] += 1
			return True
		count_univalue(root, count)
		return count[0]

def create_binarytree(root):
	if not root: return None
	start = TreeNode(root[0])
	i = 1
	q = deque([start])
	while i < len(root):
		curr = q.popleft()
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
	if not root: return ans
	q = deque([root])
	while any(q):
		curr = q.popleft()
		ans.append(curr.val if curr else None)
		if curr:
			q.append(curr.left)
			q.append(curr.right)
	return ans

root = [5, 1, 5, 5, 5, None, 5]
#output = 4
# root = [5, 4, 5, 4, 4, None, 5]
#output = 5

start = create_binarytree(root)
print(print_tree(start))
s = Solution()
print(s.univalue(start))
