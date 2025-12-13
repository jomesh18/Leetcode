'''
3321. Find X-Sum of All K-Long Subarrays II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

nums.length == n
1 <= n <= 105
1 <= nums[i] <= 109
1 <= x <= k <= nums.length
'''
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        d = {} # val: freq
        top = SortedList() # (freq, val)
        rest = SortedList() # (freq, val)
        curr_sum = 0

        def balance():
            nonlocal curr_sum
            while len(top) < x and rest:
                f1, n1 = rest.pop()
                top.add((f1, n1))
                curr_sum += f1*n1
            
            while top and rest and top[0] < rest[-1]:
                f1, n1 = top.pop(0)
                f2, n2 = rest.pop()
                top.add((f2, n2))
                rest.add((f1, n1))
                curr_sum += f2*n2 - f1*n1

        def update(val, delta):
            nonlocal curr_sum
            if val in d:
                if (d[val], val) in top:
                    top.remove((d[val], val))
                    curr_sum -= d[val]*val
                else:
                    rest.remove((d[val], val))
            d[val] = d.get(val, 0) + delta
            if d[val] == 0: del d[val]
            else: rest.add((d[val], val))
            balance()

        for i in range(k):
            update(nums[i], 1)

        ans = [curr_sum]
        for i in range(k, len(nums)):
            update(nums[i], 1)
            update(nums[i-k], -1)
            ans.append(curr_sum)
        return ans
