class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        if len(nums) < k:
            return 0
        
        mySet = set()
        total = 0
        result = 0
        left = 0
        
        for right in range(len(nums)):
            while nums[right] in mySet:
                mySet.remove(nums[left])
                total -= nums[left]
                left += 1
            
            mySet.add(nums[right])
            total += nums[right]
            
            if right - left + 1 == k:
                result = max(result, total)
                mySet.remove(nums[left])
                total -= nums[left]
                left += 1
        
        return result
