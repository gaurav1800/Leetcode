from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # slow implementation
#         if (len(s) != len(t)):
#             return False
        
#         for letter in s:
#             if (s.count(letter) != t.count(letter)):
#                 return False
#         return True
        
        # fast implementation
        return Counter(s) == Counter(t)
        