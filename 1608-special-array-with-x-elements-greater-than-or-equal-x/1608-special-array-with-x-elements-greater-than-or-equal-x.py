class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for i in range(len(nums) + 1):
            arr = [num for num in nums if num >= i]
            if len(arr) == i:
                return i
        
        return -1