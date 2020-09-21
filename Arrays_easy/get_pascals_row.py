class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        previous_row = [1, 1]
        for _ in range(2, rowIndex+1):
            current_row = []
            for j in range(len(previous_row)-1):
                current_row.append(previous_row[j]+previous_row[j+1])
            previous_row = [1]+current_row.copy()+[1]
        return previous_row

obj = Solution()
rowIndex = 4
print(obj.getRow(rowIndex))
