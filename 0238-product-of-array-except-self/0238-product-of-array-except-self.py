class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums

        product = 1
        zeroFlag = 0
        
        for num in nums:
            if num == 0:
                zeroFlag += 1
            else:
                product *= num
        
        if zeroFlag > 1:
            return [0] * len(nums)
        
        for idx, num in enumerate(nums):
            if zeroFlag == 1 and num != 0:    
                nums[idx] = 0
            elif zeroFlag == 1 and num == 0:
                nums[idx] = product
            else:
                nums[idx] = int(product/num)
        
        return nums