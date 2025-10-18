class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        negative = False

        # Whitespaces
        while i < len(s) and s[i] == " ":
            i += 1
        
        if i >= len(s): return 0
        
        s = s[i::]
        i = 0
      
        # Signedness
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                negative = True
            i += 1
            s = s[i::]
            i = 0
        
        while i < len(s) and s[i] == "0":
            i += 1
        
        if i >= len(s) or not s[i].isdigit(): return 0

        s = s[i::]
        i = 0

        while i < len(s) and s[i].isdigit():
            i += 1

        result = int(s[:i:]) if negative is False else int(s[:i:])*-1

        if result < -2**31: return -2**31
        elif result > 2**31 - 1: return 2**31 - 1
        else: return result



        






        