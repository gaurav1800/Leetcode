class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        result = 0
        stack = []
        n = len(nums)
        
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        for j in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                result = max(result, j - stack.pop())
        
        return result