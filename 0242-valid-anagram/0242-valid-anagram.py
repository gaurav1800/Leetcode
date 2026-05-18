class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # shorter soln
        if len(s) != len(t):
            return False
        
        chars = set(s)

        for c in chars:
            if s.count(c) != t.count(c):
                return False
        return True


        # longer soln        
        # kvMap = {}
        
        # for c in s:
        #     if c in kvMap:
        #         kvMap[c] += 1
        #     else:
        #         kvMap[c] = 1
        # for c in t:
        #     if c not in kvMap:
        #         return False
        #     kvMap[c] -= 1
        # for k, v in kvMap.items():
        #     if kvMap[k] != 0:
        #         return False
        
        # return True

        