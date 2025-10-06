class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        mySet = set(ransomNote)

        for c in mySet:
            if ransomNote.count(c) > magazine.count(c):
                return False

        return True

        # # slow solution
        # hashMap = {}

        # for c in magazine:
        #     if c in hashMap:
        #         hashMap[c] += 1
        #     else:
        #         hashMap[c] = 1
        
        # for c in ransomNote:
        #     if c in hashMap and hashMap[c] > 0:
        #         hashMap[c] -= 1
        #     else:
        #         return False
        
        # return True