'''
1209. Remove All Adjacent Duplicates in String II
Medium

3131

59

Add to List

Share
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
Accepted
176,014
Submissions
313,546
'''
#stack O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i, c in enumerate(s):
            if stack and stack[-1][0] == c:
                if stack[-1][1] == k-1: stack.pop()
                else: stack[-1] = (c, stack[-1][1]+1)
            else:
                stack.append((c, 1))
                
        return "".join(u*v for u, v in stack)

#two pointer O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        j = 0
        n = len(s)
        count = [1]*n
        s = list(s)
        for i in range(n):
            s[j] = s[i]
            if j>0 and s[j] == s[j-1]: count[j] = count[j-1]+1
            else: count[j] = 1
            if count[j] == k: j -= k
            j += 1
        return "".join(s[:j])