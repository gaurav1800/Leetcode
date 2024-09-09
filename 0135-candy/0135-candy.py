class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        
        fromLeft = [0] * n
        fromRight = [0] * n
        
        counter = n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                fromLeft[i] = fromLeft[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                fromRight[i] = fromRight[i+1] + 1
        
        for i in range(n):
            counter += max(fromLeft[i], fromRight[i])
        
        return counter