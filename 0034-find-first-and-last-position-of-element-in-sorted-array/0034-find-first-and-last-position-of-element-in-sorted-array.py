class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo+hi) // 2
            if target == nums[mid]:
                return self.getStartEnd(nums, mid, target)
            elif target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        
        return [-1, -1]

    def getStartEnd(self, nums: List[int], mid: int, target: int):
        start, end = mid, mid
        while start >= 0 and nums[start] == target:
            start -= 1
        while end < len(nums) and nums[end] == target:
            end += 1
        
        return[start+1, end-1]
        



