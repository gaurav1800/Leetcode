class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(numRows):
            result.append([1] * (i+1))
        
        for i in range(2, len(result)):
            for j in range(1, len(result[i])-1):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        
        return result