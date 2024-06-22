class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        array = [amount + 1] * (amount + 1)
        array[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    array[a] = min(array[a], 1 + array[a - c])
        return array[amount] if array[amount] != amount + 1 else -1