# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue = [root]
        max_lvl = 1
        lvl = 1
        max_sum = -inf
        
        while queue:
            lvl_sum = 0
            next_lvl = []
            
            for node in queue:
                lvl_sum += node.val
                
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            
            if lvl_sum > max_sum:
                max_sum = lvl_sum
                max_lvl = lvl
            
            queue = next_lvl
            lvl += 1
        
        return max_lvl