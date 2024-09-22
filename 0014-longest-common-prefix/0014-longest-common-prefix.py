class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        
        result = ""
        
        for i in range(len(strs[0])):
            j = 1
            while j < len(strs) and strs[0][i] == strs[j][i]:
                j += 1
            
            if j == len(strs):
                result += strs[0][i]
            else:
                return result
        
        return result
                