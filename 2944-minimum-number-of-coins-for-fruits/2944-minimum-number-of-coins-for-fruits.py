class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        n = len(prices)
        ans = math.inf
        
        minqueue = collections.deque([(0, n)])
        
        
        for i in range(n-1, -1, -1):
            while minqueue and minqueue[0][1] > (i+1) * 2:
                minqueue.popleft()
            ans = prices[i] + minqueue[0][0]
            
            while minqueue and minqueue[-1][0] >= ans:
                minqueue.pop()
            
            minqueue.append((ans, i))
        
        return ans