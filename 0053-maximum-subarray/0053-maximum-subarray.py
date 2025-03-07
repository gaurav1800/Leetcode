class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentSum = 0
        result = nums[0]
        
        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            result = max(result, currentSum)
        
        return result