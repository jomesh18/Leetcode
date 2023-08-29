class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        min_penalty = penalty
        ans = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                penalty -= 1
                if penalty < min_penalty:
                    ans = i+1
                    min_penalty = penalty
            else:
                penalty += 1
        return ans