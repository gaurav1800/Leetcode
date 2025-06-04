class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        sr, sc = 0, 0
        rows = len(matrix)
        cols = len(matrix[0])
        er = rows - 1
        ec = cols - 1
        
        result = []
        counter = 0
        
        while sr <= er or sc <= ec:
            for i in range(sc, ec+1):
                result.append(matrix[sr][i])
                counter += 1
            sr += 1
            if counter == rows*cols:
                return result
            
            for i in range(sr, er+1):
                result.append(matrix[i][ec])
                counter += 1
            ec -= 1
            if counter == rows*cols:
                return result
            
            for i in range(ec, sc-1, -1):
                result.append(matrix[er][i])
                counter += 1
            er -= 1
            if counter == rows*cols:
                return result
            
            for i in range(er, sr-1, -1):
                result.append(matrix[i][sc])
                counter += 1
            sc += 1
            if counter == rows*cols:
                return result
            
        
        return result