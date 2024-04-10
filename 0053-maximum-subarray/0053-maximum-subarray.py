class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = nums[0]
        currSum = 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += num
            
            result = max(result, currSum)
            
        
        return result