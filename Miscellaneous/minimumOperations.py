'''
2170. Minimum Operations to Make the Array Alternating
Medium

292

237

Add to List

Share
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

 

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
Accepted
13,516
Submissions
41,458
Seen this question in a real interview before?

Yes

No

'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1: return 0
        even, odd = Counter(nums[0::2]), Counter(nums[1::2])
        f_e, s_e, f_e_count, s_e_count = 0, 0, 0, 0
        f_o, s_o, f_o_count, s_o_count = 0, 0, 0, 0
        
        for key in odd:
            if odd[key] >= f_o_count:
                s_o, s_o_count = f_o, f_o_count
                f_o, f_o_count = key, odd[key]
            elif odd[key] >= s_o_count:
                s_o, s_o_count = key, odd[key]
        
        for key in even:
            if even[key] >= f_e_count:
                s_e, s_e_count = f_e, f_e_count
                f_e, f_e_count = key, even[key]
            elif even[key] >= s_e_count:
                s_e, s_e_count = key, even[key]
        print(odd, even)
        print(f_e, f_e_count, s_e, s_e_count)
        print(f_o, f_o_count, s_o, s_o_count)
        
        if f_e != f_o: return l - f_e_count - f_o_count
        return min(l-f_e_count-s_o_count, l-f_o_count-s_e_count)
