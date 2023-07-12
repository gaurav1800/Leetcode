class Solution {
    public int maxArea(int[] height) {
        
        int max = 0;
        int lo = 0, hi = height.length - 1;
        
        while (lo < hi) {
            int min = Math.min(height[lo], height[hi]);
            max = Math.max(max, min*(hi-lo));
            if (height[lo] < height[hi]) {
                lo++;
            }
            else {
                hi--;
            }
        }
        
        return max;
    }
}