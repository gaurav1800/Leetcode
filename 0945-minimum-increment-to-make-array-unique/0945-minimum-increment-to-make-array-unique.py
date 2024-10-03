class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        result = 0
        nums.sort()
        
        next_available = nums[0]    
        
        for num in nums:
            if num < next_available:
                result += next_available-num
            
            next_available = max(num, next_available) + 1
        
        return result