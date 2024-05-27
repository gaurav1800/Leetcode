class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        num1 = edges[0][0]
        num2 = edges[0][1]
        num3 = edges[1][0]
        num4 = edges[1][1]
        
        if num1 == num2 or num1 == num3 or num1 == num4:
            return num1
        elif num2 == num3 or num2 == num4:
            return num2
        else:
            return num3