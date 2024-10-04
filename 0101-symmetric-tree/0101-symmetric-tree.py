# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def isSymmetric(i, j):
            if not i or not j:
                return i == j
            
            return i.val == j.val and isSymmetric(i.left, j.right) and isSymmetric(i.right, j.left)
        
        return isSymmetric(root, root)
        