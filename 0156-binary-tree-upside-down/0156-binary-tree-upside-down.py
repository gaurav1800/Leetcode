# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        prevRoot = None
        prevRight = None
        
        while root:
            nextRoot = root.left
            root.left = prevRight
            prevRight = root.right
            root.right = prevRoot
            prevRoot = root
            root = nextRoot
        
        return prevRoot
            