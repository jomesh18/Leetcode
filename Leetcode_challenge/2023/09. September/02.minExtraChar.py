'''
2707. Extra Characters in a String
Medium

853

41

Add to List

Share
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
'''
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = {}
        pos = []
        for v in dictionary:
            l = []
            i = 0
            while i < len(s):
                ind = s.find(v, i)
                if ind == -1:
                    break
                l.append(ind)
                pos.append((ind, v))
                i = ind+len(v)
            if l:
                d[v] = l
        pos.sort()
        # print(d)
        # print(pos)
        memo = {}
        def helper(i):
            if i == len(pos):
                return 0
            if i in memo: return memo[i]
            not_taking = helper(i+1)
            curr_ind = pos[i][0]
            
            next_ind = pos[i][0]+len(pos[i][1])
            ans = len(pos)
            for k in range(i+1, len(pos)):
                if pos[k][0] >= next_ind:
                    ans = k
                    break
                    
            taking = len(pos[i][1])+helper(ans)
            memo[i] = max(taking, not_taking)
            return memo[i]
        using = helper(0)
        # print(using, len(s))
        # print(memo)
        return len(s)-using