class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 == 1:
            return 0
        
        return self.helper(nums, (total+target) // 2, total)
    
    def helper(self, nums, target, total):
        dp = [1] + [0] * total
        for i in range(len(nums)):
            for j in range(total, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        
        return dp[target]