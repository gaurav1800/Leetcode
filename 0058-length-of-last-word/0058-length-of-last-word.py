class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1
        result = 0

        if s[i] == " ":
            while i >= 0 and s[i] == " ":
                i -= 1

        while i >= 0:
            if s[i] == " ":
                return result
            result += 1
            i -= 1
        
        return result
