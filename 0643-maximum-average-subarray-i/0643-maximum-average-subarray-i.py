class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        i = 0
        total = 0
        while i < k:
            total += nums[i]
            i += 1
        result = total / k
        
        l, r = 0, k-1
        n = len(nums)

        total -= nums[l]
        l += 1
        r += 1

        while r < n:
            total += nums[r]
            result = max(result, total/k)
            total -= nums[l]
            l += 1
            r += 1
        
        return result

