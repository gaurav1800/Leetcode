class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # faster solution
        left = 0
        right = 0
        result = 0
        mySet = set()
        
        while right < len(s):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
                
            mySet.add(s[right])
            result = max(result, right - left + 1)
            
            right += 1
            
        return result
        
        
        
#         slow solution
#         temp = ""
#         result = 0    
#         left = 0
    
#         for left in range(len(s)):
#             temp = ""
#             right = left 
#             currentSum = 0
            
#             while right < len(s):
#                 if s[right] in temp:
#                     break
#                 else:
#                     temp += s[right]
#                     currentSum += 1
#                 right += 1
#             result = max(result, currentSum)
        
#         return result