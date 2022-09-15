'''
2007. Find Original Array From Doubled Array
Medium

1243

76

Add to List

Share
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
 

Constraints:

1 <= changed.length <= 105
0 <= changed[i] <= 105
'''
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1: return []
        count = Counter(changed)
        res = []
        if 0 in count:
            if count[0] & 1: return []
            else: 
                res.extend([0]*(count[0]//2))
                del count[0]
        for key in sorted(list(count.keys())):
            if key not in count: continue
            else: res.extend([key]*count[key])
            if key*2 not in count or count[key] > count[2*key]:
                return []
            count[2*key] -= count[key]
            del count[key]
            if count[2*key] == 0: 
                del count[2*key]
        if len(count) != 0: return []
        return res


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1: return []
        count = Counter(changed)
        if count[0] & 1: return []

        for key in sorted(count):
            if count[key] > count[2*key]:
                return []
            count[2*key] -= count[key] if key else count[key]//2
        return list(count.elements())


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dq = deque([])
        res = []
        for i in sorted(changed):
            if dq and dq[0] == i:
                dq.popleft()
            else:
                dq.append(2*i)
                res.append(i)
        if dq: return []
        return res