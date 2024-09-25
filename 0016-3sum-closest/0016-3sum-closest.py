class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        currentResult = inf
        
        
        for i, num in enumerate(nums):
            left = i+1
            right = len(nums) - 1
            
            
            while left < right:
                total = num + nums[left] + nums[right]
                
                if abs(target-total) < abs(target - currentResult):
                    currentResult = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
                
        return currentResult