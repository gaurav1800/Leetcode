class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)
        
        
        sortedNums = sorted(nums)
        maxLen = 0
        maxCurrent = 0
        
        for idx, num in enumerate(sortedNums):
            if idx < len(sortedNums)-1:
                if sortedNums[idx] == sortedNums[idx+1]:
                    continue
                
                if sortedNums[idx] + 1 == sortedNums[idx+1]:
                    maxCurrent += 1
                    maxLen = maxLen if maxLen > maxCurrent else maxCurrent
                else:
                    maxCurrent = 0
        
        return maxLen+1
#         myDict = {}
        
#         for num in nums:
#             if num-1 in myDict:
#                 myDict[num-1] = myDict
        