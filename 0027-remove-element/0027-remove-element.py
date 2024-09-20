class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        result = 0
        
        for num in nums:
            if num != val:
                nums[result] = num
                result += 1
        
        return result