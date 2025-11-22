class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        mapping = {
            2:['a', 'b', 'c'], 
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z'],
        }

        digits = str(digits)

        if len(digits) == 1:
            return mapping[int(digits)]
        elif len(digits) == 2:
            return self.getCombinations(mapping[int(digits[0])], mapping[int(digits[1])])
        else:
            return self.getCombinations(self.getCombinations(mapping[int(digits[0])], mapping[int(digits[1])]), self.letterCombinations(digits[2::]))
        

    
    def getCombinations(self, a, b):
        output = []
        for i in a:
            for j in b:
                output.append(i+j)
        return output
