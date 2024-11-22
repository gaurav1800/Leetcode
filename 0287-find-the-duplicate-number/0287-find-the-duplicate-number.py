class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        # faster solution but uses set
        res = set()
        
        for num in nums:
            if num not in res:
                res.add(num)
            else:
                return num
        
    
        
        # time limit exceeded solution due to nested loop
#         count = 0
#         n = len(nums)
        
#         for i in range(1, n+1):
#             for j in nums:
#                 if i == j:
#                     count += 1
#                 if count == 2:
#                     return i
#             count = 0
        
#         return 0
        