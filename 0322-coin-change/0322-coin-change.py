class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        array = [amount+1] * (amount+1)
        array[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    array[i] = min(array[i], 1 + array[i-coin])
        
        return array[amount] if array[amount] != amount + 1 else -1