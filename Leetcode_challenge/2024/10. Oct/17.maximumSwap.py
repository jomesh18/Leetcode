'''
670. Maximum Swap
Medium

3597

228

Add to List

Share
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        str_num = list(str(num))
        max_ = -1
        for i in range(len(str_num)-1, -1, -1):
            if int(str_num[i]) > int(str_num[max_]):
                max_ = i
            else:
                new_arr = str_num[:i]+[str_num[max_]]+str_num[i+1:]
                new_arr[max_] = str_num[i]
                # print(i, new_arr, max_)
                ans = max(ans, int(''.join(new_arr)))
        return ans