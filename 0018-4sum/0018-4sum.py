class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        solution = []
        
        if len(nums) < 4:
            return result
        
        nums.sort()
        
        def helper(k, start, target):
            if k == 2:
                left = start
                right = len(nums)-1
                
                while left < right:
                    total = nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append(solution + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
            else:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    solution.append(nums[i])
                    helper(k-1, i+1, target-nums[i])
                    solution.pop()
        
        helper(4, 0, target)
        return result
                    
                
            
                    
        