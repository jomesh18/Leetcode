'''
1395. Count Number of Teams
Medium

2874

205

Add to List

Share
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        
        for i in range(1, n-1):
            curr = rating[i]
            left_less_than, left_greater_than, right_less_than, right_greater_than = 0, 0, 0, 0
            for j in range(i):
                if curr > rating[j]:
                    left_less_than += 1
                elif curr < rating[j]:
                    left_greater_than += 1
            for j in range(i+1, n):
                if curr > rating[j]:
                    right_less_than += 1
                elif curr < rating[j]:
                    right_greater_than += 1
            ans += left_less_than * right_greater_than + left_greater_than * right_less_than
        
        return ans