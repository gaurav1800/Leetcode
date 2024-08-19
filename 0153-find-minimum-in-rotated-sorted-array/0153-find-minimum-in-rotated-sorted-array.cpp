class Solution {
public:
    int findMin(vector<int>& nums) {
        
        
        int lo = 0;
        int hi = nums.size()-1;
        
        int result = nums[lo];
        
        while(lo <= hi) {
            
            if (nums[lo] < nums[hi]) {
                return min(result, nums[lo]);
            }
            
            
            int mid = (lo+hi) / 2;
            
            result = min(result, nums[mid]);
            
            if (nums[lo] <= nums[mid]) {
                lo = mid+1;
            }
            else {
                hi = mid-1;
            }
        }
        
        return result;
    }
};