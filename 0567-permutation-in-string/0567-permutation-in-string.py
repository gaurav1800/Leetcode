class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        size = len(s1)
        s1Sorted = sorted(s1)
        
        for i in range(len(s2)):
            if i+size > len(s2):
                return False
            
            window = s2[i:i+size]
            windowSorted = sorted(window)
            
            if s1Sorted == windowSorted:
                return True
        
        return False