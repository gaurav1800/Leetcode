# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root, arr):
            if root:
                helper(root.left, arr)
                helper(root.right, arr)
                arr.append(root.val)
            return arr
        
        arr = []
        return helper(root, arr)