class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        result = 0
        counter = 0

        while columnTitle:
            letter = columnTitle[-1]

            result += (26 ** counter) * (ord(letter) - 64)

            counter += 1
            columnTitle = columnTitle[:-1] 

        return result