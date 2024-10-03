class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        
        result = 0
        
        d12 = Counter([num1 + num2 for num1 in nums1 for num2 in nums2])
        d34 = Counter([num3 + num4 for num3 in nums3 for num4 in nums4])
        
        for key, value in d12.items():
            if -key in d34:
                result += d34[-key] * value
        
        return result
        
        
        
        
        
        
        # longer solution
#         dict12 = {} 
#         dict34 = {}
        
#         counter = 0
        
#         for num1 in nums1:
#             for num2 in nums2:
#                 if num1+num2 in dict12:
#                     dict12[num1+num2] += 1
#                 else:
#                     dict12[num1+num2] = 1
        
#         for num3 in nums3:
#             for num4 in nums4:
#                 if num3+num4 in dict34:
#                     dict34[num3+num4] += 1
#                 else:
#                     dict34[num3+num4] = 1
        
#         for key, value in dict12.items():
#             if -key in dict34:
#                 counter += dict12[key]*dict34[-key]
        
#         return counter
            