class Solution:
    def lastRemaining(self, n: int) -> int:
        
        # Recursive solutoin
        if n == 1:
            return 1
        
        return 2 * (n//2  + 1 - self.lastRemaining(n//2))


        # longer solution
        # head = 1
        # step = 1
        # left = True
        # remaining = n

        # while remaining > 1:
        #     if left or remaining%2 == 1:
        #         head += step
        #     step *= 2
        #     remaining //= 2
        #     left = not left
        
        # return head