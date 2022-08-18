'''
126. Word Ladder II
Hard

4627

588

Add to List

Share
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
#bidirectional bfs
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        bq = deque([beginWord])
        eq = deque([endWord])
        bvisited = {beginWord}
        evisited = {endWord}
        found = False
        all_combo_dict = defaultdict(list)
        l = len(beginWord)
        for word in wordList:
            for i in range(l):
                all_combo_dict[word[:i]+'*'+word[i+1:]].append(word)
        parent = defaultdict(set)
        rev = False
        depth = 0
        while bq and not found:
            depth += 1
            local_visited = set()
            for _ in range(len(bq)):
                curr = bq.popleft()
                for i in range(l):
                    next_word = curr[:i]+'*'+curr[i+1:]
                    if next_word in all_combo_dict:
                        for child in all_combo_dict[next_word]:
                            if child == curr:
                                continue
                            if child not in bvisited:
                                if not rev:
                                    parent[child].add(curr)
                                else:
                                    parent[curr].add(child)
                                local_visited.add(child)
                                if child in evisited:
                                    found = True
                                bq.append(child)
            bvisited.update(local_visited)
            bq, eq, bvisited, evisited, rev = eq, bq, evisited, bvisited, not rev
        print(parent)
        res = []
        def dfs(node, path, d):
            if d == 0:
                if path[-1] == beginWord:
                    res.append(path[::-1])
                return
            for p in parent[node]:
                dfs(p, path+[p], d-1)
                
        dfs(endWord, [endWord], depth)
        return res


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        l = len(beginWord)
        all_combo = defaultdict(list)
        if beginWord not in wordList:
            for i in range(l):
                all_combo[beginWord[:i]+'*'+beginWord[i+1:]].append(beginWord)
        for word in wordList:
            for i in range(l):
                all_combo[word[:i]+'*'+word[i+1:]].append(word)
        q = {endWord}
        visited = {endWord}
        reverse = defaultdict(list)
        found = False
        while q and not found:
            new_q = set()
            for w in q:
                if w == beginWord:
                    found = True
                    break
                for i in range(l):
                    for nw in all_combo[w[:i]+'*'+w[i+1:]]:
                        if nw not in visited:
                            new_q.add(nw)
                            reverse[nw].append(w)
            visited.update(new_q)
            q = new_q
        
        res = set()
        def dfs(w, path):
            for nw in reverse[w]:
                path.append(nw)
                if nw == endWord:
                    res.add(tuple(path))
                else:
                    dfs(nw, path)
                path.pop()
                
        dfs(beginWord, [beginWord])
        return list(res)
                            