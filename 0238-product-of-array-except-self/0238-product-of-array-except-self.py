class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        q = 1
        zeroFlag = 0
        numsFlag = 0
        
        for num in nums:
            if num == 0:
                zeroFlag += 1
                continue
            else:
                numsFlag = 1
                q *= num
            
        if numsFlag == 0:
            return nums
        
        if zeroFlag > 1:
            return [0] * len(nums)

        
        for idx, num in enumerate(nums):
            if zeroFlag == 1 and num != 0:    
                nums[idx] = 0
            elif zeroFlag == 1 and num == 0:
                nums[idx] = q
            else:
                nums[idx] = int(q/num)
        
        return nums