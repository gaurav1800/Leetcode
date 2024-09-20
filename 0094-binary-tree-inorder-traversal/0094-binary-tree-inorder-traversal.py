# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        
        return self.helper(root, result)
        
        
    
    def helper(self, root, arr):
        
        if root:
            self.helper(root.left, arr)
            arr.append(root.val)
            self.helper(root.right, arr)
        
            return arr 
        