class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # 1d array extra space solution
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [0] * (n)
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                
                elif j > 0:
                    dp[j] += dp[j-1]
                    
        return dp[n-1]
        
        
        
        
#         # 2d array extra space solution
        
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
        
#         dp = [[0] * (n+1) for i in range(m+1)]
#         dp[1][0] = 1
        

#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if obstacleGrid[i-1][j-1] == 0:
#                     dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
#         return dp[m][n]
                