'''
839. Similar String Groups
Hard

2134

210

Add to List

Share
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
'''
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        k = len(strs[0])
        adj = [[] for _ in range(n)]
        
        def similar(i, j):
            word1, word2 = strs[i], strs[j]
            first = True
            pos = []
            for p in range(k):
                if word1[p] == word2[p]:
                    continue
                else:
                    pos.append(p)
                    if len(pos) > 2:
                        return False
            if not pos: return True
            if len(pos) == 1: return False
            a, b = pos
            return (word1[a] == word2[b] and word1[b] == word2[a])
                        
        def dfs(i):
            for nei in adj[i]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
                    
        for i in range(n):
            for j in range(i+1, n):
                if similar(i, j):
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited = [False]*n
        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        
        return count
                    

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        k = len(strs[0])
        adj = [[] for _ in range(n)]
        
        def similar(i, j):
            word1, word2 = strs[i], strs[j]
            diff = 0
            for p in range(k):
                if word1[p] != word2[p]:
                    diff += 1
                    if diff > 2: return False
            return (diff == 0 or diff == 2)
                        
        def dfs(i):
            for nei in adj[i]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
                    
        for i in range(n):
            for j in range(i+1, n):
                if similar(i, j):
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited = [False]*n
        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        
        return count
                    