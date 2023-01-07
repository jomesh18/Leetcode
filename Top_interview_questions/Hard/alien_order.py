'''
https://www.lintcode.com/problem/892/
892 · Alien Dictionary
Algorithms
Hard
Accepted Rate
26%
Description
Solution41
Notes99+
Discuss20
Leaderboard
Record
Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Wechat reply 【Google】 get the latest requent Interview questions. (wechat id : jiuzhang1104)


You may assume all letters are in lowercase.
The dictionary is invalid, if string a is prefix of string b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order.
The letters in one string are of the same rank by default and are sorted in Human dictionary order.
Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
'''
# post order dfs
from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        d = {c: set() for word in words for c in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    d[w1[j]].add(w2[j])
                    break
        visited = {}
        ans = []
        def dfs(i):
            if i in visited:
                return visited[i]
            visited[i] = True
            for nei in d[i]:
                if dfs(nei): return True
            visited[i] = False
            ans.append(i)

        for i in range(25, -1, -1):
            c = chr(ord('a') + i)
            if c in d and c not in visited:
                if dfs(c):
                    return ''
        ans.reverse()
        return ''.join(ans)


# topological sort using heap instead of q (for lintcode extra condition)
from typing import (
    List,
)
from heapq import *
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for word in words for c in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: return ''
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]: indegree[w2[j]] += 1
                    adj[w1[j]].add(w2[j])
                    break

        heap = [c for c in indegree if indegree[c] == 0]
        heapify(heap)
        order = []

        while heap:
            # print(indegree, heap)
            for _ in range(len(heap)):
                c = heappop(heap)
                order.append(c)
                for nei in adj[c]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        heappush(heap, nei)
        
        return ''.join(order) if len(order) == len(adj) else ''