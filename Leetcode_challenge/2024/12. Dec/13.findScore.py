'''
2593. Find Score of an Array After Marking All Elements
Medium

523

7

Add to List

Share
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.

 

Example 1:

Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
Example 2:

Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
'''
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        pq = [(num, i) for i, num in enumerate(nums)]
        heapify(pq)
        marked = [False]*len(nums)
        while pq:
            while pq and marked[pq[0][1]]:
                heappop(pq)
            if not pq: break
            num, i = heappop(pq)
            score += num
            marked[i] = True
            if i+1 < len(nums) and not marked[i+1]:
                marked[i+1] = True
            if i > 0 and not marked[i-1]:
                marked[i-1] = True
        return score