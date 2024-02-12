class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s.sort()
        # t.sort()
        
        if (len(s) != len(t)):
            return False
        
        for letter in s:
            if (s.count(letter) != t.count(letter)):
                return False
        return True
        
        # if s == t:
        #     return true
        # return false
        