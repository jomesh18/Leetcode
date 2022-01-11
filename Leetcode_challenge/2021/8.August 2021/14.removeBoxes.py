'''
 Remove Boxes

You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

Example 2:

Input: boxes = [1,1,1]
Output: 9

Example 3:

Input: boxes = [1]
Output: 1

 

Constraints:

    1 <= boxes.length <= 100
    1 <= boxes[i] <= 100

'''

# class Solution:
#     def removeBoxes(self, boxes: [int]) -> int:
#         N = len(boxes)
#         memo = [[[0]*N for _ in range(N) ] for _ in range(N) ]
        
#         def dp(i, j, k):
#             if i > j: return 0
#             if not memo[i][j][k]:
#                 m = i
#                 while m+1 <= j and boxes[m+1] == boxes[i]:
#                     m += 1
#                 i, k = m, k + m - i
#                 ans = dp(i+1, j, 0) + (k+1) ** 2
#                 for m in range(i+1, j+1):
#                     if boxes[i] == boxes[m]:
#                         ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
#                 memo[i][j][k] = ans
#             return memo[i][j][k]
    
#         return dp(0, N-1, 0)

from collections import defaultdict
class Solution:
    def removeBoxes(self, boxes: [int]) -> int:
        memo={}
        lookup = defaultdict(set)
        last={}
        st=ed=0
        while st<len(boxes):
            while ed<len(boxes) and boxes[ed]==boxes[st]:
                ed+=1
            lookup[boxes[st]].add((st,ed-1))
            for k in range(st,ed):
                last[k]=ed-1
            st=ed
        def helper(i,j,k):
            if j>last[i]:
                i,k = last[i],k+last[i]-i
            else:
                return (j-i+1+k)**2
            if i>j:
                return 0
            if (i,j,k) in memo:
                return memo[i,j,k]
            ans=(k+1)**2+helper(i+1,j,0)
            num=boxes[i]
            for l,r in lookup[num]:
                if l>i and r<=j:
                    ans=max(ans,helper(i+1,l-1,0)+helper(r,j,k+1+r-l))
            memo[i,j,k]=ans
            return ans
        return helper(0,len(boxes)-1,0)

boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23

sol = Solution()
print(sol.removeBoxes(boxes))
