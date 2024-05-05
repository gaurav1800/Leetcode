class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int result = nums[0];
        int current_sum = 0;
        
        for(int i = 0; i < nums.size(); i++) {
            if (current_sum < 0) {
                current_sum = 0;
            }
            current_sum += nums[i];
            
            result = max(result, current_sum);
        }
        
        return result;
        
    }
};