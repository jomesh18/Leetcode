'''
1029. Two City Scheduling
Medium

2841

240

Add to List

Share
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
 

Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000
Accepted
148,573
Submissions
241,681
Seen this question in a real interview before?

Yes

No


'''

#recursive without memo, tle
class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        n = len(costs)//2
        def helper(i, count_a):
            if i >= 2*n: return 0
            adda, addb = float("inf"), float("inf")
            if count_a < n:
                adda = helper(i+1, count_a+1) + costs[i][0]
            if i-count_a < n:
                addb = helper(i+1, count_a) + costs[i][1]
            return min(adda, addb)
        return helper(0, 0)


#recursive, with memo
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        memo = {}
        # @lru_cache()
        def helper(i, count_a):
            if i >= 2*n: return 0
            if (i, count_a) in memo: return memo[(i, count_a)]
            adda, addb = float("inf"), float("inf")
            if count_a < n:
                adda = helper(i+1, count_a+1) + costs[i][0]
            if i-count_a < n:
                addb = helper(i+1, count_a) + costs[i][1]
            ans = min(adda, addb)
            memo[(i, count_a)] = ans
            return ans
        return helper(0, 0)

#dp solution
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        dp = [[0]*(2*n+1) for _ in range(n+1)]
        
        for count_a in range(n, -1, -1):
            for i in range(2*n-1, -1, -1):
                adda, addb = float("inf"), float("inf")
                if count_a < n:
                    adda = dp[count_a+1][i+1] + costs[i][0]
                if i-count_a < n:
                    addb = dp[count_a][i+1] + costs[i][1]
                dp[count_a][i] = min(adda, addb)

        # print(dp)
        return dp[0][0]

#using sorting
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sum(cost[0] for cost in costs)
        refunds = sorted(cost[1]-cost[0] for cost in costs)
        return cost+sum(refunds[:len(costs)//2])

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = sorted(costs, key = lambda x: -(x[1]-x[0]))
        # print(diff)
        return sum(diff[i][0] + diff[len(costs)//2 + i][1] for i in range(len(costs)//2))


costs = [[393,874],[299,93],[947,491],[214,782],[25,158],[666,163],[547,293],[653,291],[922,106],[294,479],[79,559],[579,933],[433,507],[75,686],[420,508],[813,256],[613,936],[192,540],[463,762],[784,881],[440,260],[176,655],[532,263],[890,437],[553,516],[880,668]]


print(len(costs))

sol = Solution()
print(sol.twoCitySchedCost(costs))
