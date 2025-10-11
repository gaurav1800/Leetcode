class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        k = 0
        i = 1

        while i < len(nums):
            if nums[i] == nums[k]:
                i += 1
                            
            else:
                k += 1
                nums[k] = nums[i]
            
        return k+1