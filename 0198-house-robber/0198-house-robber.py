class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)
        
        
        
        for i in range(2, len(nums)):
            if i == 2:
                nums[2] += nums[0]
            else:
                nums[i] += max(nums[i-2], nums[i-3])

        return max(nums[-1], nums[-2])
        