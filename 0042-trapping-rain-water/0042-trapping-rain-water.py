class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]
        total = 0
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                total += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                total += rightMax - height[right]
        
        return total