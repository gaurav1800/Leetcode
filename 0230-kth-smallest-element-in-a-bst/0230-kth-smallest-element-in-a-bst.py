# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []
        
        def helper(root, arr):
            if root:
                helper(root.left, arr)
                arr.append(root.val)
                helper(root.right, arr)
                
                
        helper(root, arr)
        return arr[k-1]