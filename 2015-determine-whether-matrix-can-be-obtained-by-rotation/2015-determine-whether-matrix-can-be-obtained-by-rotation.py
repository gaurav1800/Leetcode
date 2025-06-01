class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for i in range(4):
            if mat == target:
                return True
            self.rotate90(mat)
        return False

    def rotate90(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()