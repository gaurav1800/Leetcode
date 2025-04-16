class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        counter = 0
        
        for num in nums:
            if counter < 1 or num > nums[counter-1]:
                nums[counter] = num
                counter += 1
        
        return counter