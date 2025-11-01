# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        
        def helperDfs(root: TreeNode, path: list[str]):
            if not root:
                return
            if not root.left and not root.right:
                result.append("".join(path) + str(root.val))
                return

            path.append(str(root.val) + "->")
            helperDfs(root.left, path)
            helperDfs(root.right, path)
            path.pop()
        
        helperDfs(root, [])
        return result

        