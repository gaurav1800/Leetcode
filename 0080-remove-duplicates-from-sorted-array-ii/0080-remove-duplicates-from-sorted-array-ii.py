class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 
        return k

        # longer solution
        # if len(nums) < 3:
        #     return len(nums)
        # k = 0
        # i = 0
        # while i < len(nums):
        #     num = nums[i]
        #     counter = 0
        #     while i < len(nums) and nums[i] == num:
        #         counter += 1
        #         i += 1
        #     if counter == 1:
        #         nums[k] = num
        #         k += 1
        #     if counter >= 2:
        #         nums[k], nums[k+1] = num, num
        #         k += 2
        # return k
            
            

