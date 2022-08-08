'''
307. Range Sum Query - Mutable
Medium

3865

208

Add to List

Share
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
Accepted
224,929
Submissions
556,386
'''
# Sqrt Decomposition
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        l = len(nums)**.5
        self.l = math.ceil(len(nums)/l)
        self.b = [0]*self.l
        for i in range(len(nums)):
            self.b[i//self.l] += nums[i]
        # print('init')
        # print(self.b)
        # print(self.nums)
        # print(self.l)

    def update(self, index: int, val: int) -> None:
        self.b[index//self.l] += (val-self.nums[index])
        self.nums[index] = val
        # print('update')
        # print(self.b)
        # print(self.nums)

    def sumRange(self, left: int, right: int) -> int:
        # print('rangesum')
        start_block = left//self.l
        end_block = right//self.l
        # print(start_block, end_block)
        s = 0
        if start_block == end_block:
            for i in range(left, right):
                s += self.nums[i]
        else:
            for i in range(left, (start_block+1)*(self.l)):
                s += self.nums[i]
            for i in range(start_block+1, end_block):
                s += self.b[i]
            for i in range(end_block*(self.l), right+1):
                s += self.nums[i]
        return s


#segment tree
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        
class NumArray:

    def __init__(self, nums: List[int]):
        def create_tree(l, r):
            if l > r: return None
            node = Node(l, r)
            if l == r:
                node.total = nums[l]
            else:
                mid = (l+r)//2
                node.left = create_tree(l, mid)
                node.right = create_tree(mid+1, r)
                node.total = node.left.total + node.right.total
            return node
        self.root = create_tree(0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        def update_tree(node, i, v):
            if node.start == node.end:
                node.total = v
                return 
            
            mid = (node.start+node.end)//2
            if i <= mid:
                update_tree(node.left, i, v)
            else:
                update_tree(node.right, i, v)
            node.total = node.left.total + node.right.total
            
        update_tree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def sum_range_tree(node, l, r):
            if l <= node.start and r >= node.end:
                return node.total
            elif l > node.end or r < node.start:
                return 0
            else:
                return sum_range_tree(node.left, l, r) + sum_range_tree(node.right, l, r)
            
        return sum_range_tree(self.root, left, right)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)