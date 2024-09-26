class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        start = 0
        startToIdx = {0:-1}
        
        for i, num in enumerate(nums):
            start += num
            if k != 0:
                start %= k
            if start in startToIdx:
                if i - startToIdx[start] > 1:
                    return True
            else:
                startToIdx[start] = i
        
        return False
                    
                
            
            