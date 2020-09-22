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
print(obj.getRow(rowIndex));

#from leetcode
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         count=[1]*(rowIndex+1)
#         for i in range(0,rowIndex):
#             for k in range(i,0,-1):
#                 count[k]+=count[k-1]     
#         return count

# obj = Solution()
# rowIndex = 4
# print(obj.getRow(rowIndex))
