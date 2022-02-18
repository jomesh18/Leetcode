'''
332. Reconstruct Itinerary
Hard

3632

1528

Add to List

Share
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
Accepted
267,332
Submissions
670,385
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for s, d in tickets:
            adj_list[s].append(d)
        for key in adj_list:
            adj_list[key].sort(reverse=True)
        stack, res = ["JFK"], []
        while stack:
            airport = stack[-1]
            if airport in adj_list and len(adj_list[airport]) > 0:
                stack.append(adj_list[airport].pop())
            else:
                res.append(stack.pop())
        return res[::-1]

#from leetcode stefan
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list)
        for s, d in sorted(tickets)[::1]:
            targets[s] += d,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit("JFK")
        return route[::-1]