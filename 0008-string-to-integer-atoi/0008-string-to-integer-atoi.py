class Solution:
    def reset(self, s, i):
            s = s[i::]
            i = 0
            return s, i

    def checkIfOverLength(self, s, i):
        if i == len(s): 
            return True
        return False

    def myAtoi(self, s: str) -> int:
        i = 0
        negative = False

        # Whitespaces
        while i < len(s) and s[i] == " ":
            i += 1
        
        if self.checkIfOverLength(s, i): return 0
        s, i = self.reset(s, i)
      
        # Signedness
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                negative = True
            i += 1
            s, i = self.reset(s, i)
        
        while i < len(s) and s[i] == "0":
            i += 1
        
        if self.checkIfOverLength(s, i) or not s[i].isdigit(): return 0

        s, i = self.reset(s, i)

        # Conversion
        while i < len(s) and s[i].isdigit():
            i += 1

        result = int(s[:i:]) if negative is False else int(s[:i:])*-1

        # Rounding
        if result < -2**31: return -2**31
        elif result > 2**31 - 1: return 2**31 - 1
        else: return result



        

        




        






        