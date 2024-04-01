class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo = 0
        hi = len(nums) - 1
        
        while (lo <= hi):
            mid = (lo+hi) // 2
            
            ey = nums[mid]
            
            if (target < ey):
                hi = mid-1
            elif (target > ey):
                lo = mid+1
            else:
                return mid
        
        return -1
        