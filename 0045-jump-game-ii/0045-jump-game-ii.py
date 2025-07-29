class Solution:
    def jump(self, nums: List[int]) -> int:
        
        result = 0
        reach = 0
        end = 0
        
        for i in range(len(nums) - 1):
            reach = max(reach, i+nums[i])
            if reach >= len(nums)-1:
                result += 1
                break
            
            if i == end:
                result += 1
                end = reach
        
        return result