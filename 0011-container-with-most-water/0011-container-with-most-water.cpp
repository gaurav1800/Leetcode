class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int left = 0;
        
        int right = height.size() - 1;
        
        int result = 0;
        
        while(left < right) {
            int area = (right - left) * min(height[left], height[right]);
            
            if (area > result) {
                result = area;
            }
            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return result;
        
    }
};