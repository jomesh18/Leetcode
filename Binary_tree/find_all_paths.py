'''
find all paths in a binary tree

i/p: root = [3,5,1,6,2,0,8,null,null,7,4]
o/p: [[3, 5, 6], [3, 5, 2, 7], [3, 5, 2, 4], [3, 1, 0], [3, 1, 8]]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
	
def find_paths(start):
	res = []
	def helper(node, discovered):
		if not node: return
		discovered.append(node)
		if not node.left and not node.right:
			res.append(discovered[:])
			discovered.remove(node)
			return
		helper(node.left, discovered)
		helper(node.right, discovered)
		discovered.remove(node)
	helper(start, [])
	ans = []
	for l in res:
		ans.append([i.val for i in l])
	return ans

def build_tree(root):
	start = TreeNode(root[0])
	q = [start]
	i = 1
	while i<len(root):
		curr = q.pop(0)
		if curr is not None:
			curr.left = TreeNode(root[i]) if root[i] is not None else None
			i += 1
			curr.right = TreeNode(root[i]) if root[i] is not None else None
			q.extend([curr.left, curr.right])
		i += 1
	return start

def print_tree(start):
	res = []
	q = [start]
	while any(q):
		curr = q.pop(0)
		if curr:
			res.append(curr.val)
			q.extend([curr.left, curr.right])
		else:
			res.append(None)
	return res

root = [3,5,1,6,2,0,8,None,None,7,4]
# o/p: [[3, 5, 6], [3, 5, 2, 7], [3, 5, 2, 4], [3, 1, 0], [3, 1, 8]]
start = build_tree(root)
print(print_tree(start))
print(find_paths(start))
