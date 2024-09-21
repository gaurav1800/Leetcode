class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        
        n = len(ratings)
        
        leftToRight = [0] * n
        rightToLeft = [0] * n
        
        counter = n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                leftToRight[i] = leftToRight[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightToLeft[i] = rightToLeft[i+1] + 1
        
        for i in range(n):
            counter += max(leftToRight[i], rightToLeft[i])
        
        return counter
        