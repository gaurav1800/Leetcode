# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        que = collections.deque()
        
        if root:
            que.append(root)

        while que:
            val = []

            for i in range(len(que)):
                node = que.popleft()
                val.append(node.val)
                
                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
                    
            result.append(val)
        
        return result
        