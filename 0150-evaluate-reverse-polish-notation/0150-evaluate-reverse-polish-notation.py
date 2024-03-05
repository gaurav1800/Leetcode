class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        ops = ["+", "-", "*", "/"]
        
        for char in tokens:
            if char in ops:
                if char == "+":
                    stack.append(stack.pop() + stack.pop())
                elif char == "-":
                    first, second = stack.pop(), stack.pop()
                    stack.append(second - first)
                elif char == "*":
                    stack.append(stack.pop() * stack.pop())
                elif char == "/":
                    first, second = stack.pop(), stack.pop()
                    stack.append(int(second / first))
            else:
                stack.append(int(char))
        
        return stack[0]
        