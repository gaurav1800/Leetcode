class Solution:
    def partitionString(self, s: str) -> int:
        
        counter = 0
        
        sub = ""
        
        for i in range(len(s)):
            if sub.count(s[i]) == 0:
                sub = sub+s[i]
            else:
                sub = s[i]
                counter += 1
            
        return counter+1
        