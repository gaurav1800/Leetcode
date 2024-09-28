class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currentMin = inf
        result = 0
        
        for price in prices:
            if price < currentMin:
                currentMin = price
            else:
                result = max(result, price-currentMin)
        
        return result
        