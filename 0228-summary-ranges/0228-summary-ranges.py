class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        i = 0
        result = []
        while i < len(nums):
            start = nums[i] 
            while i+1 < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            
            result.append(f"{start}" if start == nums[i] else f"{start}->{nums[i]}")
            i += 1
        
        return result