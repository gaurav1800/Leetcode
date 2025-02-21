"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def helper(root, arr):
            if root:
                arr.append(root.val)
                for child in root.children:
                    helper(child, arr)
            return arr
        
        result = []
        
        return helper(root, result)
        