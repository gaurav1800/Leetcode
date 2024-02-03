class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        length = len(arr)
        
        array = [0] * (length + 1)
        
        for i in range(1, length+1):
            maxi = -math.inf
            for j in range(1, min(i, k) + 1):
                maxi = max(maxi, arr[i - j])
                array[i] = max(array[i], array[i - j] + maxi * j)
        
        return array[-1]