'''
997. Find the Town Judge
Easy

2596

187

Add to List

Share
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
Accepted
223,482
Submissions
445,060
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        common = [set() for _ in range(n)]
        for person, trusted in trust:
            common[person-1].add(trusted-1)
        none = set()
        judges = {i for i in range(n)}
        for i, sets in enumerate(common):
            if not sets:
                none.add(i)
            else:
                judges = judges.intersection(sets)
        print(judges, none)
        return none.pop()+1 if none and len(none) == 1 and none == judges else -1

# O(t+n) time, O(n) space
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = [0] * (n+1)
        for u, v in trust:
            degree[u] -= 1
            degree[v] += 1
        for i in range(1, n+1):
            if degree[i] == n-1:
                return i
        return -1