class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        currentNum = 0
        result = ''

        for char in s:
            if char.isdigit():
                currentNum = currentNum * 10 + int(char)
            else:
                if char == '[':
                    stack.append((result, currentNum))
                    result = ''
                    currentNum = 0
                elif char == ']':
                    prevStr, num = stack.pop()
                    result = prevStr + num * result
                else:
                    result += char

        return result