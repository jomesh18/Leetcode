'''
2222. Number of Ways to Select Buildings
Medium

281

9

Add to List

Share
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

 

Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.
Accepted
8,738
Submissions
19,786
Seen this question in a real interview before?

Yes

No

'''
#O(n), O(1)
class Solution:
    def numberOfWays(self, s: str) -> int:
        #a, b are number of 1 and 0 after ith building
        ans = 0
        a, b = 0, 0
        for ch in s:
            if ch == "1": a += 1
            else: b += 1
        
        # c, d are number of 1 and 0 before ith building
        c, d = 0, 0
        for ch in s:
            if ch == '1':
                ans += b*d
                a -= 1
                c += 1
            else:
                ans += a*c
                b -= 1
                d += 1
        return ans

dp, O(n), O(n)
class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {'0': 0, '1': 0, '01': 0, '010': 0, '10': 0, '101': 0}
        
        for  c in s:
            if c == '1':
                dp['1'] += 1
                dp['01'] += dp['0']
                dp['101'] += dp['10']
            else:
                dp['0'] += 1
                dp['10'] += dp['1']
                dp['010'] += dp['01']
        return dp['010'] + dp['101']

class Solution {
    public long numberOfWays(String s) {
        long ans = 0;
        int len = s.length();
        
        long totZeros = 0;
        
        for(int i=0;i<len;i++){
            totZeros += s.charAt(i)=='0'?1:0;
        }
        
        long totOnes = len - totZeros;
        
        long currZeros = s.charAt(0)=='0'?1:0;
        long currOnes = s.charAt(0)=='1'?1:0;
        
        for(int i=1;i<len;i++){
            if(s.charAt(i) == '0'){
                ans = ans + (currOnes * (totOnes-currOnes));
                currZeros++;
            }else{
                ans = ans + (currZeros * (totZeros-currZeros));
                currOnes++;
            }
        }
        return ans;
    }
}