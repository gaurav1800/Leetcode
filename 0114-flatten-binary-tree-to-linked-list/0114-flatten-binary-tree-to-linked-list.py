# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        
        while root:
            if root.left:
                rightMost = root.left
                while rightMost.right:
                    rightMost = rightMost.right
                
                rightMost.right = root.right
                root.right = root.left
                root.left = None
            
            root = root.right
        