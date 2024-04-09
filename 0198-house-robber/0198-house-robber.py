class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        first, second = 0, 0
        
        for num in nums:
            temp = max(num+first, second)
            first = second
            second = temp
        
        return second
        
        
        
        
#         if (len(nums) == 1):
#             return nums[0]
        
#         if (len(nums) == 2):
#             return max(nums[0], nums[1])
            
        
#         mylist = []
        
#         mylist.append(nums[0])
#         mylist.append(nums[1])
        
        
#         for i in range(2, len(nums)):
#             mylist.append(max(nums[i] + mylist[i-2], max(mylist)))
            
#         return max(mylist[-1], mylist[-2])
        
