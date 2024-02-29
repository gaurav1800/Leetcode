class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
#         faster implementation
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0]*26, [0]*26
        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 
            s2Count[ord(s2[i]) - ord('a')] += 1 
        
        matches = 0
        
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
            
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[right]) - ord('a')
            
            s2Count[idx] += 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s2Count[idx] - 1 == s1Count[idx]:
                matches -= 1
                
                
            idx = ord(s2[left]) - ord('a')
            
            s2Count[idx] -= 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s2Count[idx] + 1 == s1Count[idx]:
                matches -= 1
                
            left += 1
            
        return matches == 26
                                
            
        
        
#         slow implementation
#         size = len(s1)
#         s1Sorted = sorted(s1)
        
#         for i in range(len(s2)):
#             if i+size > len(s2):
#                 return False
            
#             window = s2[i:i+size]
#             windowSorted = sorted(window)
            
#             if s1Sorted == windowSorted:
#                 return True
        
#         return False