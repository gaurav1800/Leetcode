class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def dfs(left:int, right:int, s:str) -> None:
            if left == 0 and right == 0:
                result.append(s)
            if left > 0:
                dfs(left-1, right, s+'(')
            if left < right:
                dfs(left, right - 1, s+')')
        
        dfs(n, n, '')
        return result