class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int product = 1;
        int flag = 0;
        
        for(int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                flag += 1;
                continue;
            }
            product *= nums[i];
        }
        
        vector<int> result(nums.size(), product);
        
        if (flag == 0) {
            for(int i = 0; i < nums.size(); i++) {
                result[i] /= nums[i];
            }
        }
        else if (flag > 1) {
            for(int i = 0; i < nums.size(); i++) {
                result[i] = 0;
            }
        }
        else {
            for(int i = 0; i < nums.size(); i++) {
                if (nums[i] == 0) {
                    result[i] = product;
                }
                else {
                    result[i] = 0;
                }
            }
        }
        
        return result;
        
        
    }
};