class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashMap = {}
        for i, c in enumerate(s):
            if c in hashMap and hashMap[c] != t[i]:
                return False
            elif c not in hashMap:
                hashMap[c] = t[i]
        
        hashMap = {}
        for i, c in enumerate(t):
            if c in hashMap and hashMap[c] != s[i]:
                return False
            elif c not in hashMap:
                hashMap[c] = s[i]
        
        return True