class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(s, target, path):
            if target < 0:
                return
            if target == 0:
                result.append(path.copy())  
                return
            for i in range(s, len(candidates)):
                path.append(candidates[i])
                dfs(i, target - candidates[i], path)  
                path.pop()
        

        dfs(0, target, [])
        return result
