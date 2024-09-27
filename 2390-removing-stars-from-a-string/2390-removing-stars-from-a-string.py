class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if stack and char == "*":
                stack.pop()
            elif not stack and char == "*":
                continue
            else:
                stack.append(char)
        
        return "".join(stack)
                
        