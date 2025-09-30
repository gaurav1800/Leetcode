class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashMap = {}
        for i, c in enumerate(s):
            if c in hashMap and hashMap[c] != t[i]:
                return False
            elif c not in hashMap and t[i] in hashMap.values():
                return False
            else:
                hashMap[c] = t[i]
        return True