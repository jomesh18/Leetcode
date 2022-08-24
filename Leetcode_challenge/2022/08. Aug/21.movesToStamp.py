'''
936. Stamping The Sequence
Hard

1346

206

Add to List

Share
You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
place stamp at index 0 of s to obtain "abc??",
place stamp at index 1 of s to obtain "?abc?", or
place stamp at index 2 of s to obtain "??abc".
Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

 

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".
 

Constraints:

1 <= stamp.length <= target.length <= 1000
stamp and target consist of lowercase English letters.
'''
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        done = [False]*n
        ans = []
        A = []
        q = deque()
        for i in range(n-m+1):
            made, todo = set(), set()
            for j in range(m):
                if stamp[j] == target[i+j]:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))
            if not todo:
                ans.append(i)
                for j in range(i, i+m):
                    if not done[j]:
                        done[j] = True
                        q.append(j)
        while q:
            i = q.popleft()
            for j in range(max(0, i-m+1), min(n-m, i)+1):
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for k in A[j][0]:
                            if not done[k]:
                                q.append(k)
                                done[k] = True
        return ans[::-1] if all(done) else []


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        slen, tlen = len(stamp), len(target)
        s_covers = set()
        
        for i in range(slen):
            for j in range(slen-i):
                s_covers.add('#'*i+stamp[i:slen-j]+'#'*j)
        
        done = '#'*tlen
        ans = []
        while target != done:
            found = False
            for i in range(tlen-slen, -1, -1):
                if target[i:i+slen] in s_covers:
                    found = True
                    ans.append(i)
                    target = target[:i]+'#'*slen+target[i+slen:]
            if not found:
                return []
        return ans[::-1]