'''
2448. Minimum Cost to Make Array Equal
Hard

1092

13

Add to List

Share
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

 

Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.
 

Constraints:

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106
'''
# O(nlogn)
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        new_nums = sorted((nums[i], cost[i]) for i in range(n))
        pre_cost = [0]*n
        pre_cost[0] = new_nums[0][1]
        for i in range(1, n):
            pre_cost[i] = new_nums[i][1] + pre_cost[i-1]
        
        total_cost = 0
        for i in range(1, n):
            total_cost += new_nums[i][1]*(new_nums[i][0]-new_nums[0][0])
            
        ans = total_cost
        
        for i in range(1, n):
            gap = new_nums[i][0]-new_nums[i-1][0]
            total_cost += gap*pre_cost[i-1]
            total_cost -= gap*(pre_cost[n-1]-pre_cost[i-1])
            ans = min(ans, total_cost)
        return ans

# binary search O(nlogk) where k is max-min
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        def get_cost(val):
            ans = 0
            for i in range(n):
                ans += cost[i]*abs(nums[i]-val)
            return ans
        answer = get_cost(nums[0])
        l, r = min(nums), max(nums)
        while l < r:
            mid = (l+r)//2
            cost1 = get_cost(mid)
            cost2 = get_cost(mid+1)
            answer = min(cost1, cost2)
            if cost1 <= cost2:
                r = mid
            else:
                l = mid + 1
        return answer