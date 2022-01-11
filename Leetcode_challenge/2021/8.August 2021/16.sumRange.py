'''
Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

 

Constraints:

    1 <= nums.length <= 104
    -105 <= nums[i] <= 105
    0 <= left <= right < nums.length
    At most 104 calls will be made to sumRange.

'''
#my try
# class NumArray:

#     def __init__(self, nums: [int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         return sum([self.nums[i] for i in range(left, right+1)])

#from leetcode
class NumArray:
    def __init__(self, nums):
        self.sum_array=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sum_array[i+1]=self.sum_array[i]+nums[i]
            
    def sumRange(self, left, right):
        return self.sum_array[right+1]-self.sum_array[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

null = None

inp1 = ["NumArray", "sumRange", "sumRange", "sumRange"]
inp2 = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output = [null, 1, -1, -3]

sol = NumArray(inp2[0][0])

res = [None]
for fn, para in zip(inp1, inp2):
    if fn == "sumRange":
        res.append(sol.sumRange(para[0], para[1]))
    else:
        continue

print(Output)
print(res)
print(res == Output)
