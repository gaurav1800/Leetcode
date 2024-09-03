class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int currentSum = INT_MIN;
        int result = INT_MIN;
        
        for(int num : nums) {
            
            if (currentSum < 0) {
                currentSum = num;
            }
            else {
                currentSum += num;    
            }
            
            result = max(result, currentSum);
        }
        
        return result;
        
    }
};