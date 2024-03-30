class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums)-1
        
        result = nums[lo]
        
        while (lo <= hi):
            if nums[lo] <= nums[hi]:
                result = min(result, nums[lo])
                break
            
            mid = (lo+hi) // 2
            result = min(nums[mid], result)
            
            if nums[lo] <= nums[mid]:
                lo = mid+1
            else:
                hi = mid-1
        
        return result