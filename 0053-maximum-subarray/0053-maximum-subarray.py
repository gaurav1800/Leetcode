class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSubArray = nums[0]
        currSum = 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += num
            
            maxSubArray = max(maxSubArray, currSum)
        
        return maxSubArray