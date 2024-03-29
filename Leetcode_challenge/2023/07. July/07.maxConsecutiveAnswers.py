'''
2024. Maximize the Confusion of an Exam
Medium

1580

27

Add to List

Share
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

 

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
 

Constraints:

n == answerKey.length
1 <= n <= 5 * 104
answerKey[i] is either 'T' or 'F'
1 <= k <= n
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answerKey = list(answerKey)
        def count(p):
            curr = 0
            l = 0
            ans = 0
            for r in range(len(answerKey)):
                # print(r, l, ans, r-l+1, curr)
                if answerKey[r] == p:
                    ans = max(ans, r-l+1)
                    continue
                else:
                    curr += 1
                    if curr <= k:
                        ans = max(ans, r-l+1)
                        continue
                    else:
                        while curr > k:
                            if answerKey[l] != p:
                                curr -= 1
                            l += 1
                # print(r, l, ans, r-l+1, curr)
            return ans
        
        return max(count("T"), count("F"))
    


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = Counter(answerKey[:k])
        ans = k
        l = 0
        for i in range(k, len(answerKey)):
            count[answerKey[i]] += 1
            while min(count['T'], count['F']) > k:
                count[answerKey[l]] -= 1
                l += 1
            ans = max(ans, i-l+1)
        return ans


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = Counter()
        max_size = 0
        for i in range(len(answerKey)):
            count[answerKey[i]] += 1
            minor = min(count['T'], count['F'])
            if minor <= k:
                max_size += 1
            else:
                count[answerKey[i-max_size]] -= 1
        return max_size