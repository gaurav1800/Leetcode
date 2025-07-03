class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        for string in path.split('/'):
            if string == '' or string == '.': # do nothing
                continue
            if string == '..': # move back in the path
                if stack:
                    stack.pop()
            else: # move forward
                stack.append(string)

        return '/' + '/'.join(stack)