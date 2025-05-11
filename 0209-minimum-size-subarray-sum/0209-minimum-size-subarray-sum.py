class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        result = math.inf
        total = 0
        j = 0

        for i, num in enumerate(nums):
            total += num
            while total >= target:
                result = min(result, i - j + 1)
                total -= nums[j]
                j += 1

        return 0 if result == math.inf else result