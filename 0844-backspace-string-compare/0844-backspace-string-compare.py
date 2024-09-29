class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sStack = []
        tStack = []
        
        for char in s:
            if char == "#" and sStack:
                sStack.pop()
            elif char != "#":
                sStack.append(char)
                
        for char in t:
            if char == "#" and tStack:
                tStack.pop()
            elif char != "#":
                tStack.append(char)
        
        return "".join(sStack) == "".join(tStack) 
        