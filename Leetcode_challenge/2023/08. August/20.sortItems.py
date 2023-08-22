'''
1203. Sort Items by Groups Respecting Dependencies
Hard

1579

268

Add to List

Share
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 

Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
'''
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        def topo_sort(graph, indegree):
            q = []
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    q.append(i)
            ans = []
            while q:
                nq = []
                for i in q:
                    ans.append(i)
                    for nei in graph[i]:
                        indegree[nei] -= 1
                        if indegree[nei] == 0:
                            nq.append(nei)
                q = nq
            return ans
                
      
        group_id = m
        
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
                
        item_graph = defaultdict(list)
        item_indegree = [0]*n
        group_graph = defaultdict(list)
        group_indegree = [0]*group_id
        
        for i, before_list in enumerate(beforeItems):
            for j in before_list:
                item_graph[j].append(i)
                item_indegree[i] += 1
                if group[j] != group[i]:
                    group_graph[group[j]].append(group[i])
                    group_indegree[group[i]] += 1
                    
        item_order = topo_sort(item_graph, item_indegree)
        # print(item_order, item_graph, item_indegree)
        if len(item_order) != len(item_graph): return []
        
        group_order = topo_sort(group_graph, group_indegree)
        # print(group_order)
        if len(group_order) != len(group_graph): return []
        
        ordered_groups = defaultdict(list)
        
        for item in item_order:
            ordered_groups[group[item]].append(item)
            
        ans = []
        
        for group_i in group_order:
            ans.extend(ordered_groups[group_i])
            
        return ans