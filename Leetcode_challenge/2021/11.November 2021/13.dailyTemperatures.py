'''
739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

 

Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100

'''
# class Solution:
#     def dailyTemperatures(self, temperatures: [int]) -> [int]:
#         ans = [0]*len(temperatures)
#         stack = [0]
#         for i in range(1, len(temperatures)):
#             while stack and temperatures[stack[-1]] < temperatures[i]:
#                 index = stack.pop()
#                 ans[index] = i-index 
#             stack.append(i)
#         return ans

class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        ans = [0] * len(temperatures)
        hottest = temperatures[-1]
        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i] >= hottest:
                # ans[i] = 0
                hottest = temperatures[i]
            else:
                index_to_check = i + 1
                while temperatures[i] >= temperatures[index_to_check]:
                    index_to_check += ans[index_to_check]
                ans[i] = index_to_check - i
            print(ans)
        return ans

temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# 
# temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# temperatures = [30,60,90]
# # Output: [1,1,0]

temperatures = [89,62,70,58,47,47,46,76,100,70]
# Output: [8,1,5,4,3,2,1,1,0,0]

temperatures = [34,80,80,34,34,80,80,80,80,34]


sol = Solution()
print(sol.dailyTemperatures(temperatures))
