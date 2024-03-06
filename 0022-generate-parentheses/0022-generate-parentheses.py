class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        result = []
        
        def backtrack(opening, closing):
            if opening == closing == n:
                result.append("".join(stack))
            
            if opening < n:
                stack.append("(")
                backtrack(opening+1, closing)
                stack.pop()
            
            if closing < opening:
                stack.append(")")
                backtrack(opening, closing+1)
                stack.pop()
        
        backtrack(0, 0)
        
        return result
        
# #         using DFS
#         result = []
        
#         def dfs(left:int, right:int, s:str) -> None:
#             if left == 0 and right == 0:
#                 result.append(s)
#             if left > 0:
#                 dfs(left-1, right, s+'(')
#             if left < right:
#                 dfs(left, right - 1, s+')')
        
#         dfs(n, n, '')
#         return result
        