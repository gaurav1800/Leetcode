# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
#         first implementation
#         def build(l: int, r: int) -> Optional[TreeNode]:
#             if l > r:
#                 return None
#             m = (l+r)//2
            
#             return TreeNode(nums[m],
#                            build(l, m-1),
#                            build(m+1, r))
#         return build(0, len(nums) - 1)
        
        
#         second implementation
        def build(arr):
            if not arr: 
                return None
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            node.left = build(arr[:mid])
            node.right = build(arr[mid+1:])
            return node
        return build(nums)
        