class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
        if (nums.empty())
          return 0;

        vector<int> dp(nums.size(), 1);

        for (int i = 1; i < nums.size(); ++i) {
          for (int j = 0; j < i; ++j) {
            if (nums[j] < nums[i])
              dp[i] = max(dp[i], dp[j] + 1);
            }
        }


        int result = INT_MIN;
        
        for (int num : dp) {
            result = max(num, result);    
        }
        
        return result;
    }
    
};