class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        result = []

        for i, char in enumerate(expression):
            if char in '+-*':
                for x in self.diffWaysToCompute(expression[:i]):
                    for y in self.diffWaysToCompute(expression[i + 1:]):
                        result.append(eval(str(x) + char + str(y)))

        return result or [int(expression)]