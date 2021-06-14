'''
Maximum Performance of a Team
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 

Constraints:

1 <= <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108
   Hide Hint #1  
Keep track of the engineers by their efficiency in decreasing order.
   Hide Hint #2  
Starting from one engineer, to build a team, it suffices to bring K-1 more engineers who have higher efficiencies as well as high speeds.

'''
# import heapq
# class Solution:
#     def maxPerformance(self, n: int, speed: [int], efficiency: [int], k: int) -> int:
#         modulo = 10 ** 9 + 7

#         # build tuples of (efficiency, speed)
#         candidates = zip(efficiency, speed)
#         # sort the candidates by their efficiencies
#         candidates = sorted(candidates, key=lambda t:t[0], reverse=True)

#         speed_heap = []
#         speed_sum, perf = 0, 0
#         for curr_efficiency, curr_speed in candidates:
#             # maintain a heap for the fastest (k-1) speeds
#             if len(speed_heap) > k-1:
#                 speed_sum -= heapq.heappop(speed_heap)
#             heapq.heappush(speed_heap, curr_speed)

#             # calculate the maximum performance with the current member as the least efficient one in the team
#             speed_sum += curr_speed
#             perf = max(perf, speed_sum * curr_efficiency)

#         return perf % modulo


import heapq
class Solution:
    def maxPerformance(self, n: int, speed: [int], efficiency: [int], k: int) -> int:
        candidates = sorted(zip(efficiency, speed), key= lambda x: x[0], reverse=True)
        speed_heap, speed_sum, perf = [], 0, 0
        for curr_eff, curr_speed in candidates:
            while len(speed_heap)>k-1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            perf = max(perf, speed_sum * curr_eff)
        return perf % (10**9+7)

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
s = Solution()
print(s.maxPerformance(n, speed, efficiency, k))
