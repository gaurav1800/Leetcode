class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        length = len(nums)
        
        for i in range(1 << length):
            result.append([nums[j] for j in range(length) if (i & (1 << j))])
        
        return result
        