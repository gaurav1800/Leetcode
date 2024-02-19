class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # faster implementation
        numsSet = set(nums)
        
        maxCurrent = 0
        maxLen = 0
        
        for n in numsSet:
            if n-1 not in numsSet:
                maxCurrent = 1
                nCurrent = n
                
                while nCurrent+1 in numsSet:
                    maxCurrent += 1
                    nCurrent += 1
                    
                maxLen = max(maxCurrent, maxLen)
        
        return maxLen
        
        
        
        
        # slower implementation
#         if len(nums) < 2:
#             return len(nums)
                
#         sortedNums = sorted(nums)
#         maxLen = 0
#         maxCurrent = 0
        
#         for idx, num in enumerate(sortedNums):
#             if idx < len(sortedNums)-1:
#                 if sortedNums[idx] == sortedNums[idx+1]:
#                     continue
                
#                 if sortedNums[idx] + 1 == sortedNums[idx+1]:
#                     maxCurrent += 1
#                     maxLen = maxLen if maxLen > maxCurrent else maxCurrent
#                 else:
#                     maxCurrent = 0
        
#         return maxLen+1
