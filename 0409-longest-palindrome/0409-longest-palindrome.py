class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        result = 0
        
        myMap = {}
        
        for c in s:
            if c not in myMap:
                myMap[c] = 0
            myMap[c] += 1
        
        for key in myMap.keys():
            result += myMap[key]//2
        
        result *= 2
        
        if len(s) > result:
            return result + 1
        else:
            return result
        