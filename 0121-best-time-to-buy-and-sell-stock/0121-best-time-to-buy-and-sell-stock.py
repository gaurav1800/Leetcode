class Solution:
    def maxProfit(self, prices: List[int]) -> int:

#         faster implementation
        profit = 0
        latestMin = prices[0]
        
        for price in prices:
            if price - latestMin > profit:
                profit = price - latestMin
            if price < latestMin:
                latestMin = price
        
        return profit
        
        
        
#         slow implementation

#         left = 0
#         right = 1
        
#         maxProfit = 0
        
#         while right < len(prices):
#             if (prices[right] < prices[left]):
#                 left = right
#                 right += 1
#                 continue
#             else:
#                 maxProfit = max(maxProfit, prices[right] - prices[left])
#                 right += 1
        
#         return maxProfit