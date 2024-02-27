class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        temp = ""
        result = 0
        
        left = 0
        
        for left in range(len(s)):
            temp = ""
            right = left 
            currentSum = 0
            
            while right < len(s):
                if s[right] in temp:
                    break
                else:
                    temp += s[right]
                    currentSum += 1
                right += 1
            result = max(result, currentSum)
        
        return result
                
        